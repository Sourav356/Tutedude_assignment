from flask import Flask, jsonify
import json

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return "Hello, World!"


# API Route
@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


# Run App
if __name__ == "__main__":
    app.run(debug=True)