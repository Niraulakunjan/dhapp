from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "status": "success",
        "message": "Hello from your new Python App on cPanel!",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    app.run(debug=True)
