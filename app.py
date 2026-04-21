from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Calculator API is running!"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input provided"}), 400

    try:
        a = float(data.get('a'))
        b = float(data.get('b'))
        op = data.get('operation')
    except:
        return jsonify({"error": "Invalid input"}), 400

    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        if b == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        result = a / b
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})