from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/algorithm', methods=['POST'])
def run_algorithm():
    data = request.get_json()
    result = custom_algorithm(data)
    return jsonify({'result': result})
@app.route('/algorithm/status', methods=['GET'])
def get_algorithm_status():
    status = "Der Algorithmus ist aktiv und bereit zur Verarbeitung von Anfragen."
    return jsonify({'status': status})

def custom_algorithm(data):
    result = sum(data)
    return result

if __name__ == '__main__':
    app.run(debug=True)
