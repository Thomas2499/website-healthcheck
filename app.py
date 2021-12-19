from flask import Flask, Response, request
from werkzeug.exceptions import BadRequest
from create_env import create_env
from config import HOST, PORT
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/create-env", methods=["POST"])
def create():
    websites = request.json
    if type(websites) is not list:
        raise BadRequest("Request body must be a list")
    addresses = create_env(websites)
    return Response(str(addresses), 200)


app.run(host=HOST, port=PORT)
