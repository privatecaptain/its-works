from main import db
from controllers import generate_id
import datetime as dt
import inspect

class User(db.Model):

	id = db.Column(db.String(255),primary_key=True)
	first_name =  db.Column(db.String(255))
	last_name =  db.Column(db.String(255))
	email =  db.Column(db.String(255))
	username =  db.Column(db.String(255))
	password =  db.Column(db.String(255))
	email_confirmed =  db.Column(db.Boolean)
	last_checkin =  db.Column(db.DateTime)
	active = db.Column(db.Boolean)
	parent = db.Column(db.String(255))

	def __init__(self,d):
		self.id = generate_id()
		members = inspect.getmembers(User,predicate=inspect.isdatadescriptor)
		members = [i[0] for i in members]
		for k,v in d.items():
			if k in members:
				setattr(self,k,v)


class Task(db.Model):

	id = db.Column(db.String(255),primary_key=True)
	name = db.Column(db.String(255))
	description = db.Column(db.String(255))
	start_time = db.Column(db.DateTime)
	end_time = db.Column(db.DateTime)
	deadline = db.Column(db.DateTime)
	created_by = db.Column(db.String(255))
	created_at = db.Column(db.DateTime)
	assignee  = db.Column(db.String(255))
	complete = db.Column(db.Boolean,default=False)
	extended = db.Column(db.Boolean,default=False)
	parent_task = db.Column(db.String(255))

	def is_complete():
		return self.complete

	def is_late():
		if self.deadline > dt.datetime.now():
			return True
		return False

	def __init__(self,d):
		self.id = generate_id()
		self.start_time = dt.datetime.now()
		self.created_at = dt.datetime.now()
		members = inspect.getmembers(Task,predicate=inspect.isdatadescriptor)
		members = [i[0] for i in members]
		for k,v in d.items():
			if k in members:
				setattr(self,k,v)











