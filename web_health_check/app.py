from threading import Thread

from flask import Flask, Response
from flask_cors import CORS

from config import HOST, PORT
from health_check import website
from scheduler import create_scheduled_check

app = Flask(__name__)
CORS(app)


@app.route("/status", methods=["GET"])
def status():
    return Response(website["status"], 200)


schedule_thread = Thread(target=create_scheduled_check)
schedule_thread.start()

app.run(host=HOST, port=PORT)
