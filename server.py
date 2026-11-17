#!/usr/bin/env python3
"""
Simple local server for Colorado Water Rights Research Assistant.
Proxies DWR API calls to avoid CORS issues.

Usage:
  pip install flask flask-cors requests
  python server.py
Then open http://localhost:5000
"""

from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__, static_folder='.')
CORS(app)

DWR_BASE = "https://dwr.state.co.us/Rest/GET/api/v2"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/<path:endpoint>')
def proxy(endpoint):
    url = f"{DWR_BASE}/{endpoint}"
    params = request.args.to_dict()
    try:
        resp = requests.get(url, params=params, timeout=30)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Colorado Water Rights Research Assistant")
    print("Open http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
