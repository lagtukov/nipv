from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route("/")
def hello():
    return "NIPV test v3"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"))