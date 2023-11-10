from flask import Flask, request, jsonify

app = Flask(__name__)

def pure_function(x):
    return x * 2

def non_pure_function(x):
    global global_variable
    global_variable = x
    return x * 2

@app.route('/function-properties', methods=['POST'])
def function_properties():
    data = request.get_json()

    function_type = data.get('function_type')
    input_value = data.get('input_value')

    if function_type == 'pure':
        result = pure_function(input_value)
    elif function_type == 'non_pure':
        result = non_pure_function(input_value)
    else:
        return jsonify({'error': 'Invalid function type'}), 400

    return jsonify({
        'function_type': function_type,
        'input_value': input_value,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
