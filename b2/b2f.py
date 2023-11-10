from flask import Flask

app = Flask(__name__)


def add_numbers(a, b):
    return f"Sum: {a + b}"


def multiply_numbers(a, b):
    return f"Product: {a * b}"


def perform_operation(operation_func, a, b):
    return operation_func(a, b)


@app.route('/calculate/<int:num1>/<int:num2>/<operation>')
def calculate_route(num1, num2, operation):
    result = 0
    if operation == 'add':
        result = perform_operation(add_numbers, num1, num2)
    elif operation == 'multiply':
        result = perform_operation(multiply_numbers, num1, num2)

    return result


if __name__ == '__main__':
    app.run(debug=True)
