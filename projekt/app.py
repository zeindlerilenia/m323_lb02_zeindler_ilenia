from flask import Flask, request, jsonify

app = Flask(__name__)

# Funktionen für den Taschenrechner
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division durch Null ist nicht erlaubt"
    return a / b

# Route für die Berechnung
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data['operation']
    num1 = data['num1']
    num2 = data['num2']

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        return jsonify({'error': 'Ungültige Operation'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
