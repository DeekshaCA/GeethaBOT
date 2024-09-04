# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ab')
def ab():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(debug=True)

