from main import db,generate_id
import datetime 
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
	



class Task(db.Model):

	id = db.Column(db.String(255),primary_key=True)
	name = db.Column(db.String(255))
	description = db.Column(db.String(255))
	start_time = db.Column(db.DateTime)
	end_time = db.Column(db.DateTime)
	deadline = db.Column(db.DateTime)
	assignee = db.Column(db.String(255))
	owner  = db.Column(db.String(255))
	complete = db.Column(db.Boolean)
	extended = db.Column(db.Boolean)

	def is_complete():
		return self.complete

	def is_late():
		if self.deadline > datetime.datetime.now():
			return True
		return False

	def __init__(self,d):
		self.id = generate_id()
		members = inspect.getmembers(Task,predicate=inspect.isdatadescriptor)
		members = [i[0] for i in members]
		for k,v in d.items():
			if k in members:
				setattr(self,k,v)







