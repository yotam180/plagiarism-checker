from flask import Flask, Response, send_from_directory, request

import time

from document_parser import Document
from entity_selection import random_entity_select
from googler import cross_search
from content_scrape import get_page_contents
from document_compare import DocumentComparer, TargetDocument


app = Flask(__name__)


def clean_newlines(x):
    return str(x).replace("\n", "\\n")


def message(text: str) -> str:
    return f"data: {clean_newlines(text)}\n\n"


def do_text_processing(article: str):
    doc = Document(article)
    ents, weights = doc.get_weighted_entities()
    selected_ents = random_entity_select(ents, weights)

    yield message("Searching similar articles...")
    for i, length, results in cross_search(selected_ents):
        yield message(f"Searching similar articles... {i*100//length}%: {results}")

    comparer = DocumentComparer(doc)

    for url, _ in results:
        yield message(f"Checking article at {url}")

        article_text = get_page_contents(url)
        comparer.compare_to(TargetDocument(url, article_text))

    yield message(comparer.as_json)


@app.route("/process", methods=["POST"])
def process_text_endpoint():
    article_to_check = str(request.data, "utf-8")

    return Response(
        do_text_processing(article_to_check),
        mimetype="text/event-stream")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("templates", path)

@app.route("/")
def index():
    return send_from_directory("templates", "index.html")

app.run(debug=True, port=8080)
