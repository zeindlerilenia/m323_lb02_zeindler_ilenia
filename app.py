from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Speicher für Notizen und Kategorien
notes = []
categories = []

# Route für die Startseite
@app.route('/')
def index():
    return render_template('index.html', notes=notes, categories=categories)

# Route zum Hinzufügen einer neuen Notiz
@app.route('/add_note', methods=['POST'])
def add_note():
    note_text = request.form.get('note_text')
    category = request.form.get('category')
    notes.append({'text': note_text, 'category': category})
    return redirect(url_for('index'))

# Eine "pure function" zum Filtern von Notizen nach Kategorie
def filter_notes_by_category(category):
    return [note for note in notes if note['category'] == category]

# Route zum Anzeigen von Notizen nach Kategorie
@app.route('/category/<category>')
def view_category(category):
    category_notes = filter_notes_by_category(category)
    return render_template('category.html', category=category, notes=category_notes)

if __name__ == '__main__':
    app.run(debug=True)
