from flask import render_template, request,flash, redirect, url_for,session,Flask
from app import app, db
from app.models import *

@app.route("/",methods=['GET','POST'])
def hello():
	m=0
	s=''
	if(request.method=='POST'):
		a= elephant.query.filter_by(comment=request.form['message']).first()
		if(a==None):
			db.session.add(elephant(request.form['message'],1))
			db.session.commit()
		else:
			a.times+=1
			print 'I worked'
		c=elephant.query.all()
		for i in c:
			if(i.times>m):
				m=i.times
				s=i.comment
			print m
			print 'asd'
	return render_template("main.html",a=s)
