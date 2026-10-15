# sample-app.py
from flask import Flask, render_template
import os

# Flask-applicatie aanmaken
app = Flask(__name__)

# Route naar de hoofdpagina
@app.route('/')
def home():
    return render_template('index.html')

# Maak tempdir als die nog niet bestaat
if not os.path.exists('tempdir'):
    os.makedirs('tempdir')

# Start de applicatie
if __name__ == "__main__":
    print("PF1 Python Webapp gestart op http://127.0.0.1:5000")
    app.run(debug=True)
