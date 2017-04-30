from app import db
class color(db.Model):
	__tablename__="element"	
	name=db.Column(db.String(100),primary_key=True)
	rang= db.Column(db.String(100),nullable=False )
	def __init__(self, name,rang):
		self.name =name
		self.rang =rang

class last(db.Model):
	__tablename__="last"	
	id=db.Column(db.Integer, primary_key=True, autoincrement=True)
	colo= db.Column(db.String(100),nullable=False)
	def __init__(self,colo):
		self.colo =colo