from flask import Flask, jsonify

app = Flask(__name__)

# Beispiel-Daten
user_data = [
    {"id": 1, "name": "John", "age": 25},
    {"id": 2, "name": "Jane", "age": 30},
    {"id": 3, "name": "Bob", "age": 22},
]

# Map: Extrahiere Namen
names = list(map(lambda x: x["name"], user_data))

# Filter: Behalte Benutzer unter 30 Jahren
young_users = list(filter(lambda x: x["age"] < 30, user_data))

# Reduce: Berechne die durchschnittliche Altersdifferenz
age_diff_sum = sum(map(lambda x: x["age"] - 25, user_data))
average_age_diff = age_diff_sum / len(user_data)

@app.route('/')
def index():
    return jsonify({
        "names": names,
        "young_users": young_users,
        "average_age_diff": average_age_diff
    })

if __name__ == '__main__':
    app.run(debug=True)
