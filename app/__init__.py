from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')