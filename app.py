from flask import (Flask, redirect, url_for, render_template, request, jsonify)
from pymongo import MongoClient
import requests
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('sheilamenu.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/special-offers')
def specialoffers():
    return render_template('special-offers.html')




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


