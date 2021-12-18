from scheduler import create_scheduled_check
from flask import Flask, Response
from health_check import website
from config import HOST, PORT
from threading import Thread
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/status", methods=["GET"])
def status():
    return Response(website["status"], 200)


schedule_thread = Thread(target=create_scheduled_check)
schedule_thread.start()

app.run(host=HOST, port=PORT)
