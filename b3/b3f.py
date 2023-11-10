from flask import Flask, request

app = Flask(__name__)

# Lambda-Funktion für die Verarbeitung der Argumente
process_arguments = lambda arg1, arg2: f"Result: {arg1.upper()} {arg2.lower()}"

@app.route('/')
def index():
    return 'Flask Lambda App'

@app.route('/process', methods=['POST'])
def process():
    # JSON-Daten mit den Argumenten im Request-Körper erwarten
    data = request.get_json()

    # Überprüfen, ob die erwarteten Argumente vorhanden sind
    if 'arg1' in data and 'arg2' in data:
        # Lambda-Funktion aufrufen und das Ergebnis zurückgeben
        result = process_arguments(data['arg1'], data['arg2'])
        return result
    else:
        return 'Error: Missing arguments.'

if __name__ == '__main__':
    app.run(debug=True)
