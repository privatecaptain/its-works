from flask import Flask,render_template,request,make_response,redirect,url_for,session,Response
from flask.ext.sqlalchemy import SQLAlchemy
import json
from flask.ext.login import LoginManager,login_user,logout_user,login_required,current_user
from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.bcrypt import Bcrypt

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
app.config['SERVER_NAME'] = 'localhost:5000'


app.config['SECRET_KEY'] = 'faefea%$W#^TGV%$*$&^DSG'


# DB instance init
db = SQLAlchemy(app)




from models import *

@app.route('/')
def index():
	return render_template('index.html')



@app.route('/task/<text:id>',methods=['GET','POST','PUT','DELETE'])
def task():

	if request.method == 'POST':
		params = request.form
		task = Task(params)
		commit(task)
		return str(task.id)

	return render_template('create_task.html')


# The MakeMyLifeEasier Functions

def commit(obj):
	db.session.add(obj)
	db.session.commit()

def mark_complete(task):
	task.complete = True
	commit(task)




if __name__ == '__main__':
	app.run()











