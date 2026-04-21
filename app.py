from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Calculator API is running!"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    a = float(data['a'])
    b = float(data['b'])
    op = data['operation']

    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        result = a / b if b != 0 else "Cannot divide by zero"
    else:
        return jsonify({"error": "Invalid operation"})

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)