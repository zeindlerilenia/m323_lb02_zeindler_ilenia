from flask import Flask, render_template
app = Flask(__name__)

# Beispiel-Daten
data = [
    {'name': 'Alice', 'age': 28},
    {'name': 'Bob', 'age': 22},
    {'name': 'Charlie', 'age': 25},
]

# Lambda-Ausdruck zum Sortieren nach Alter
sort_by_age = lambda x: x['age']

@app.route('/')
def index():
    # Sortiere die Daten nach dem Lambda-Ausdruck
    sorted_data = sorted(data, key=sort_by_age)
    return render_template('index.html', data=sorted_data)

if __name__ == '__main__':
    app.run(debug=True)
