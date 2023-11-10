from flask import Flask, jsonify

app = Flask(__name__)

# Beispiel für ein immutables Objekt (String)
immutable_string = "Immutable String"

# Beispiel für ein mutables Objekt (Liste)
mutable_list = ["Mutable", "List"]

# Endpoint für den immutablen Wert
@app.route('/immutable')
def get_immutable_value():
    return jsonify({"immutable_value": immutable_string})

# Endpoint für den mutablen Wert
@app.route('/mutable')
def get_mutable_value():
    return jsonify({"mutable_value": mutable_list})

# Endpoint zum Ändern des mutablen Werts
@app.route('/change_mutable')
def change_mutable_value():
    mutable_list[0] = "Changed"
    return jsonify({"message": "Mutable value changed successfully", "new_mutable_value": mutable_list})

if __name__ == '__main__':
    app.run(debug=True)
