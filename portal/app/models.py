from app import db
class elephant(db.Model):
	__tablename__="elephant"
	id=db.Column(db.Integer, primary_key=True, autoincrement=True)
	comment= db.Column(db.String(100),nullable=False)
	times=db.Column(db.Integer,nullable=False)
	def __init__(self,comment,times):
		self.comment =comment
		self.times =times	
