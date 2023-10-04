from pymongo import MongoClient
import jwt
from datetime import datetime, timedelta
import hashlib
from flask import (Flask,render_template,jsonify,request,redirect,url_for,session)

from werkzeug.utils import secure_filename

app = Flask(__name__)
MONGODB_CONNECTION_STRING ='mongodb+srv://test:sparta@cluster0.jrmp0f9.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient (MONGODB_CONNECTION_STRING)
db = client.dbsansco_projectpkl

SECRET_KEY ='SPARTA'


app.config['TEMPLATES_AUTO_RELOAD'] = True
# yang di uplod tersimpan disini
app.config['UPLOAD_FOLDER'] = './static/profile_pics'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)