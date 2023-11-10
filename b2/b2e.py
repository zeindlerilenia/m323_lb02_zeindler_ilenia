from flask import Flask

app = Flask(__name__)

def create_closure(func):
    def closure(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Ergebnis der Funktion: {result}"
    return closure

def example_function(x, y):
    return x + y

@app.route('/')
def home():
    closure_function = create_closure(example_function)
    result = closure_function(3, 4)
    return f"<p>{result}</p>"

if __name__ == '__main__':
    app.run(debug=True)
