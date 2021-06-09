from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    pass
@app.route('/standings')
def standings():
    pass
@app.route('/trends')
def trends():
    pass
@app.route('/method')
def method():
    pass
