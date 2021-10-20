from gevent import monkey
monkey.patch_all()

from flask import Flask, Response, send_from_directory, request

import json

from document_parser import Document
from entity_selection import random_entity_select
from googler import cross_search
from content_scrape import get_pages_contents
from document_compare import DocumentComparer, TargetDocument


app = Flask(__name__)


def clean_newlines(x):
    return str(x).replace("\n", "\\n")


def message(_type: str, text: str) -> str:
    return f'data: {json.dumps({"type": _type, "text": text})}\n\n'


def do_text_processing(article: str):
    try:
        doc = Document(article)
        ents, weights = doc.get_weighted_entities()
        selected_ents = random_entity_select(ents, weights)

        yield message("LOADING", "Searching similar articles...")
        # for i, length, results in cross_search(selected_ents):
        #     yield message("LOADING", f"Searching similar articles... {i*100//length}%")

        results = cross_search(selected_ents)

        comparer = DocumentComparer(doc)

        yield message("LOADING", "Fetching articles...")
        urls = [url for url, _ in results]
        articles = get_pages_contents(urls)

        yield message("LOADING", "Processing articles...")
        for url, article_text in zip(urls, articles):
            comparer.compare_to(TargetDocument(url, article_text))

        yield message("DONE", comparer.as_json)
    except Exception as e:
        yield message("ERROR", "Server error: " + str(e))
        raise


@app.route("/process", methods=["POST"])
def process_text_endpoint():
    article_to_check = str(request.data, "utf-8")

    return Response(
        do_text_processing(article_to_check),
        mimetype="text/event-stream",
        headers={
            "Access-Control-Allow-Origin": "*"
        })


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("templates", path)

@app.route("/")
def index():
    return send_from_directory("templates", "index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
