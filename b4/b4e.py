from flask import Flask, jsonify, request

app = Flask(__name__)

# Beispiel-Daten für die Demonstration
data = [1, 2, 3, 4, 5]


@app.route('/process', methods=['POST'])
def process():
    operation = request.json.get('operation')

    if operation == 'map':
        result = list(map(lambda x: x * 2, data))
    elif operation == 'filter':
        result = list(filter(lambda x: x % 2 == 0, data))
    elif operation == 'reduce':
        from functools import reduce
        result = reduce(lambda x, y: x + y, data)
    else:
        result = None

    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True)
