from flask import Flask, jsonify

app = Flask(__name__)

# Ursprüngliche Funktion mit schlechter Lesbarkeit
def unglesbarer_code(name):
    return 'H3ll0, ' + name + '!'

# Refaktorierte Funktion für bessere Lesbarkeit
def freundliche_begrüßung(name):
    return f'Hallo, {name}!'

# Route für die ursprüngliche Funktion
@app.route('/unglesbar/<name>', methods=['GET'])
def unlesbare_route(name):
    return jsonify({'message': unglesbarer_code(name)})

# Route für die refaktorierte Funktion
@app.route('/lesbar/<name>', methods=['GET'])
def lesbare_route(name):
    return jsonify({'message': freundliche_begrüßung(name)})

if __name__ == '__main__':
    app.run(debug=True)
