import os, socket, logging
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
app = Flask(__name__)
POD = os.getenv("POD_NAME", socket.gethostname())

@app.route("/")
def hello():
    logging.info("Handled request from %s by pod %s", request.remote_addr, POD)
    return jsonify(message="Hello World", pod=POD)

@app.route("/health")
def health():
    return jsonify(status="ok")