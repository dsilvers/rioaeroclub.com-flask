from flask import Flask, render_template
from flask_cors import cross_origin, CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/airport/*": {"origins": "*"}})


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/pancakes')
def pancakes():
    return render_template('pancakes.html')


@app.route('/membership')
def membership():
    return render_template('membership.html')


@app.route('/airport')
def airport():
    return render_template('airport.html')


@app.route('/aircraft')
def aircraft():
    return render_template('aircraft.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')
