from flask import Flask, jsonify

app = Flask(__name__)

# Vor dem Refactoring
@app.route('/monolithisch', methods=['GET'])
def monolithisch():
    a = "Hallo"
    b = "Welt"
    result = complex_function(a, b)
    return jsonify({"result": result})

def complex_function(a, b):
    # Komplexer Code hier
    return f"{a} {b}!"

# Nach dem Refactoring
@app.route('/refactored', methods=['GET'])
def refactored():
    greeting = "Hallo"
    world = "Welt"
    result = helper_function(greeting, world)
    return jsonify({"result": result})

def helper_function(greeting, world):
    # Extrahierter Code hier
    return f"{greeting} {world}!"

if __name__ == '__main__':
    app.run(debug=True)
