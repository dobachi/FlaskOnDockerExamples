from flask import request
from flask import jsonify

from ..utils import senseless_print

from ...main import app

@app.route("/get_ip", methods=["GET"])
def get_ip():
        return jsonify({'ip': request.remote_addr}), 200
