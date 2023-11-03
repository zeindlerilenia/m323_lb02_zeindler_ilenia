from flask import Flask, request, jsonify

app = Flask(__name__)

# Funktion zur Erhöhung einer Zahl um 1
def increase_number(number):
    return number + 1

# Funktion zur Verringerung einer Zahl um 1
def decrease_number(number):
    return number - 1

@app.route('/')
def home():
    return "Willkommen! Dies ist eine Flask-Anwendung zur Demonstration von B1F."

@app.route('/increase', methods=['POST'])
def increase():
    data = request.get_json()
    if 'number' in data:
        number = data['number']
        result = increase_number(number)
        return jsonify({'result': result})
    return jsonify({'error': 'Ungültige Anfrage'}), 400

@app.route('/decrease', methods=['POST'])
def decrease():
    data = request.get_json()
    if 'number' in data:
        number = data['number']
        result = decrease_number(number)
        return jsonify({'result': result})
    return jsonify({'error': 'Ungültige Anfrage'}), 400

if __name__ == '__main__':
    app.run(debug=True)
