from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "reusable-workflow-python-api"
    })

@app.route("/api/users")
def users():
    return jsonify([
        {"id": 1, "name": "David"},
        {"id": 2, "name": "Micheal"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
