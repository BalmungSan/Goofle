from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return 'hue'

app.run(debug = True, port = 8000)
