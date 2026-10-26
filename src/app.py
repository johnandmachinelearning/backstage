from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)


@app.route('/api/v1/details')
def details():
    return jsonify({
        'hostname': socket.gethostname(),
        'time': datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    })

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({
        'message': 'Testing this cicd pipeline'
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0")

# Use self hosted runners