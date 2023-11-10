from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint für das Quadrieren von zwei Zahlen
@app.route('/quadrat', methods=['POST'])
def quadrat():
    try:
        # Die JSON-Anfrage sollte ein Objekt mit den beiden Zahlen enthalten
        data = request.get_json()
        zahl1 = data['zahl1']
        zahl2 = data['zahl2']

        # Lambda-Funktion zum Quadrieren
        quadriere = lambda x: x**2

        # Quadrieren der beiden Zahlen
        ergebnis_zahl1 = quadriere(zahl1)
        ergebnis_zahl2 = quadriere(zahl2)

        # Ergebnisse als JSON zurückgeben
        result = {
            'ergebnis_zahl1': ergebnis_zahl1,
            'ergebnis_zahl2': ergebnis_zahl2
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
