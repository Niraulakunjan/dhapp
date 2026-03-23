from flask import Flask, jsonify

import requests
import time

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "status": "success",
        "message": "Hello from your new Python App on cPanel!",
        "version": "1.0.0"
    })

@app.route('/test-connection')
def test_connection():
    target_url = "https://care.dishhome.com.np/Account/Login"
    start = time.time()
    try:
        response = requests.get(target_url, timeout=10)
        duration = time.time() - start
        return jsonify({
            "status": "success",
            "remote_status_code": response.status_code,
            "duration": f"{duration:.2f}s",
            "message": "Connected to DishHome from New App"
        })
    except Exception as e:
        duration = time.time() - start
        return jsonify({
            "status": "error",
            "duration": f"{duration:.2f}s",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
