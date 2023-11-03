from flask import Flask, request, render_template

app = Flask(__name__)

# Beispiel für eine pure function
def add_numbers(a, b):
    return a + b

@app.route('/')
def home():
    return "Willkommen zur Funktionen-Erklärungsanwendung!"

@app.route('/pure_function')
def pure_function():
    description = "Eine pure function ist eine Funktion, die für die gleichen Eingabewerte immer denselben Ausgabewert zurückgibt. Sie hat keine Nebeneffekte und ändert den Zustand der Anwendung nicht."

    return render_template('function_description.html', title="Pure Function", description=description)

@app.route('/procedure')
def procedure():
    description = "Eine Prozedur ist eine Folge von Anweisungen, die eine Aufgabe ausführt. Sie kann den Zustand der Anwendung ändern und hat in der Regel Nebeneffekte."

    return render_template('function_description.html', title="Prozedur", description=description)

if __name__ == '__main__':
    app.run(debug=True)
