import uuid

def generate_id():
	return str(uuid.uuid4().hex)


def send_mail(to,subject,text):
	pass

def make_mail_body(task):
	pass

def reminder(task):
	pass

def request_extension(task):
	pass

def approve_extension(task):
	pass

def reject_extension(task):
	pass

def create_subtask(task,d):
	pass


