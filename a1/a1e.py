from flask import Flask, jsonify

app = Flask(__name__)

# Objektorientierte Programmierung (OO)
class GreetingHandler:
    def get_greeting(self):
        return "Hello, Flask with OO!"

greeting_handler = GreetingHandler()

# Prozedurale Programmierung
def get_procedural_greeting():
    return "Hello, Flask with procedural programming!"

# Funktionale Programmierung
def get_functional_greeting():
    return "Hello, Flask with functional programming!"

@app.route('/oo')
def hello_oo():
    return jsonify(message=greeting_handler.get_greeting())

@app.route('/procedural')
def hello_procedural():
    return jsonify(message=get_procedural_greeting())

@app.route('/functional')
def hello_functional():
    return jsonify(message=get_functional_greeting())

if __name__ == '__main__':
    app.run(debug=True)
