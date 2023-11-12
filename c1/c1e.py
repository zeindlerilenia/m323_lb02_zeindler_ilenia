from flask import Flask, request, jsonify
import ast
import sys
from io import StringIO

app = Flask(__name__)

def refactor_code(code):
    try:
        # Führe das Refactoring durch (hier nur ein Dummy-Beispiel)
        # In der Realität müsstest du hier deine Refactoring-Logik implementieren
        tree = ast.parse(code)
        # Hier könnte der Refactoring-Code stehen, der das AST (Abstract Syntax Tree) manipuliert
        result_code = compile(tree, filename="<string>", mode="exec")
        return result_code
    except Exception as e:
        return str(e)

@app.route('/refactor', methods=['POST'])
def refactor():
    data = request.get_json()

    if 'code' not in data:
        return jsonify({'error': 'Code fehlt im Anfragekörper'}), 400

    code = data['code']
    refactored_code = refactor_code(code)

    return jsonify({'result': refactored_code})

if __name__ == '__main__':
    app.run(debug=True)
