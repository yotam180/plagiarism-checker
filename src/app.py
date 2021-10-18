from flask import Flask, Response, send_from_directory

import time


app = Flask(__name__)


@app.route("/process", methods=["POST"])
def process_text():
    print("hello")
    def stream():
        for i in range(3):
            time.sleep(2)
            yield 'data: {"a": 5}\n\n'

    return Response(stream(), mimetype="text/event-stream")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("templates", path)

@app.route("/")
def index():
    return send_from_directory("templates", "index.html")

app.run(debug=True, port=8080)
