from flask import Flask, request, jsonify

app = Flask(__name__)

# Hier können Sie Ihre zusammenhängenden Algorithmen implementieren
def algorithm_function(input_data):
    # Hier implementieren Sie Ihren Algorithmus
    # Beispiel: Rückgabe der Länge einer Liste
    return len(input_data)

@app.route('/algorithm', methods=['POST'])
def run_algorithm():
    try:
        # JSON-Daten vom Client erhalten
        data = request.json

        # Überprüfen, ob das erforderliche Datenfeld vorhanden ist
        if 'input_data' not in data:
            return jsonify({'error': 'Fehlende Eingabedaten'}), 400

        # Eingabe für den Algorithmus erhalten
        input_data = data['input_data']

        # Algorithmus ausführen
        result = algorithm_function(input_data)

        # Ergebnis zurückgeben
        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
