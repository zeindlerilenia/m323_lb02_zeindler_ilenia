from flask import Flask

app = Flask(__name__)

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

# Funktion als Objekt in einer Variable speichern
message_function = greet

@app.route('/hello/<name>')
def hello_route(name):
    return message_function(name)

# Funktion wechseln, um eine andere Route zu bedienen
message_function = farewell

@app.route('/goodbye/<name>')
def goodbye_route(name):
    return message_function(name)

if __name__ == '__main__':
    app.run(debug=True)
