from flask import Flask, render_template

app = Flask(__name__)

# Beispielalgorithmus
def beispiel_algorithmus(input_data):
    input_data = "Beispielwert"
    ergebnis = beispiel_algorithmus(input_data)
    print("Das Ergebnis des Algorithmus für '{}': {}".format(input_data, ergebnis))

@app.route('/')
def index():
    # Einfache HTML-Seite mit Erläuterung des Algorithmus
    algorithmus_beschreibung = "Der Beispielalgorithmus nimmt einen Eingabewert und gibt ein verarbeitetes Ergebnis zurück. Hier ist eine kurze Erläuterung des Algorithmus."
    return render_template('index.html', algorithmus_beschreibung=algorithmus_beschreibung)

@app.route('/execute/<input_data>')
def execute_algorithm(input_data):
    # Aufruf des Algorithmus mit dem übergebenen Eingabewert
    ergebnis = beispiel_algorithmus(input_data)
    return "Das Ergebnis des Algorithmus für '{}': {}".format(input_data, ergebnis)

if __name__ == '__main__':
    app.run(debug=True)
