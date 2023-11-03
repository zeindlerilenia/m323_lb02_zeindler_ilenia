from flask import Flask, request, jsonify

app = Flask(__name__)

# Beispiel-Daten in einer Liste von immutablen Werten
students = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/add_student', methods=['POST'])
def add_student():
    new_student = request.json
    # Immutable: Eine neue Liste mit dem hinzugefügten Studenten wird erstellt
    updated_students = students + [new_student]
    return jsonify(updated_students)

if __name__ == '__main__':
    app.run(debug=True)
