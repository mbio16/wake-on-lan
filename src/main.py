import os
import logging
from flask import Flask, request, jsonify
from log import set_logging
from flask.logging import default_handler
from flask_endpoints import default_get, default_post, default_404

app = Flask(__name__)
app.logger.removeHandler(default_handler)


@app.route("/", methods=["GET", "POST"])
def default_route():
    if request.method == "GET":
        return default_get()
    elif request.method == "POST":
        return default_post(request)
    else:
        return default_404()


def main(app: Flask) -> None:
    log_level: str = str(os.environ.get("LOG_LEVEL", "WARNING"))
    port: int = int(os.environ.get("PORT", "8080"))
    set_logging(log_level)
    app.run(
        host="0.0.0.0",
        port=port,
        debug=(log_level == "DEBUG"),
    )


if __name__ == "__main__":
    main(app)
