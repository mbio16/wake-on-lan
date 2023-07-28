from flask import Flask, request, jsonify, make_response, wrappers
import logging
from wake_on_an import WOL

CONTENT_JSON = "application/json"


def default_get() -> wrappers.Response:
    return make_response(
        jsonify({"supported_methods": "POST"}),
        200,
    )


def default_post(request: wrappers.Request) -> wrappers.Response:
    if request.headers.get("Content-Type") == CONTENT_JSON:
        try:
            json_body = request.get_json()
            print(json_body)
            wol = WOL(
                json_body.get("mac"),
                json_body.get("ip_address"),
                json_body.get("port"),
            )
            wol.send_packet()
            return make_response(
                jsonify({}),
                200,
            )
        except Exception as e:
            return make_response(
                jsonify({"error":str(e)}),
                403,
            )
    else:
        return make_response("", 404)


def default_404() -> wrappers.Response:
    return make_response(
        jsonify({"supported_methods": ["GET", "POST"]}),
        404,
    )
