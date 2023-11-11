from flask import Flask, jsonify
from functools import reduce

app = Flask(__name__)

# Beispiel-Liste
numbers = [1, 2, 3, 4, 5]

# Funktionen für map, filter und reduce
def square(x):
    return x ** 2

def is_even(x):
    return x % 2 == 0

def multiply(x, y):
    return x * y

# Endpunkt für Quadratzahlen
@app.route('/map', methods=['GET'])
def map_endpoint():
    mapped_result = list(map(square, numbers))
    return jsonify({'result': mapped_result})

# Endpunkt für gerade Zahlen
@app.route('/filter', methods=['GET'])
def filter_endpoint():
    filtered_result = list(filter(is_even, numbers))
    return jsonify({'result': filtered_result})

# Endpunkt für das Produkt aller Zahlen
@app.route('/reduce', methods=['GET'])
def reduce_endpoint():
    reduced_result = reduce(multiply, numbers)
    return jsonify({'result': reduced_result})

if __name__ == '__main__':
    app.run(debug=True)
