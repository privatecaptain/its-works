from flask import Flask,render_template,request,make_response,redirect,url_for,session
import requests
from flask.ext.sqlalchemy import SQLAlchemy
import json
import os
from werkzeug import secure_filename
import uuid
from flask.ext.login import LoginManager,login_user,logout_user,login_required,current_user
from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__,static_url_path="/static")
app.debug = True


# #LoginManager Instansiated
login_manager = LoginManager()

# #LoginManager Initialized
login_manager.init_app(app) 

login_manager.login_view = 'login'


# Bcrypt Config

bcrypt = Bcrypt(app)


SECRET_KEY = '$&^&B&*^*MN&*CDMN&*()B^&*()P^&_N*NM(P)*&D()&*^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:badman1108@localhost/itsworks'



app.config['SECRET_KEY'] = 'faefea%$W#^TGV%$*$&^DSG'


# DB instance init
db = SQLAlchemy(app)


def generate_id():
	return str(uuid.uuid4().hex)


from models import *

@app.route('/')
def index():
	return render_template('index.html')



@app.route('/create-task',methods=['GET','POST'])
def create_task():

	if request.method == 'POST':
		params = request.form
		task = Task(params)
		db.session.add(task)
		db.session.commit()
		return str(task.id)

	return render_template('create_task.html')





if __name__ == '__main__':
	app.run()











