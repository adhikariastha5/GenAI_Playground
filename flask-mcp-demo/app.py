from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.post("/echo")
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify(received=data)

@app.post("/add")
def add():
    data = request.get_json(silent=True) or {}
    try:
        a = float(data.get("a", 0))
        b = float(data.get("b", 0))
    except (TypeError, ValueError):
        return jsonify(error="a and b must be numbers"), 400
    return jsonify(result=a + b)

if __name__ == "__main__":
    # Dev server on http://127.0.0.1:5000
    app.run(debug=True)
