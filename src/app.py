from flask import Flask, Response

import time


app = Flask(__name__)


@app.route("/")
def hello():
    
    def stream():
        for i in range(3):
            time.sleep(2)
            yield 'data: {"a": 5}\n\n'

    return Response(stream(), mimetype="text/event-stream")


app.run(debug=True, port=8080)
