# from flask import render_template, request,flash, redirect, url_for,session,Flask
# from app import app, db
# from app.models import *
# @app.route('/',methods=['GET','POST'])
# def defaa():
# 	# db.session.add(color('Potassium dichromate','Orange'))
# 	# db.session.add(color('Potassium permanganate','Violet'))
# 	# db.session.add(color('Friferric tetraoxide','Black'))
# 	# db.session.add(color('Ferrous sulphate','Green'))
# 	# db.session.add(color('Ferric sulphate','Yellow'))
# 	# db.session.add(color('Ferric hydroxide','Green'))
# 	# db.session.add(color('Ferrous hydroxide','Orange'))
# 	# db.session.add(color('Ferrous chloride','Yellow'))
# 	# db.session.add(color('Ferric chloride','Reddish brown'))
# 	# db.session.add(color('Iron (II) carbonate','Brown'))
# 	# db.session.add(color('Iron (III) nitrate','Red'))
# 	# db.session.add(color('Iron (II) sulphide','Black'))
# 	# db.session.add(color('Iron (III) sulphide','Black'))
# 	# db.session.add(color('Copper carbonate','Green'))
# 	# db.session.add(color('Copper nitrate','Bluish green'))
# 	# db.session.add(color('Copper sulphate','Blue'))
# 	# db.session.add(color('Anhydrous copper sulphate','White'))
# 	# db.session.add(color('Copper sulphide','Black'))
# 	# db.session.add(color('Copper chloride','Yellow'))
# 	# db.session.add(color('Copper (II) oxide','Black'))
# 	# db.session.add(color('Copper (I) oxide','Red'))
# 	# db.session.add(color('Copper hydroxide','Blue'))
# 	# db.session.add(color('Red lead','Red'))
# 	# db.session.add(color('Lead iodide','Yellow'))
# 	# db.session.add(color('Lead sulphide','Black'))
# 	# db.session.add(color('Lead (II) oxide','Yellow'))
# 	# db.session.add(color('Lead (IV) oxide','Brown'))
# 	# db.session.add(color('Mercuric sulphide','Black'))
# 	# db.session.add(color('Mercuric oxide','Orange red'))
# 	# db.session.add(color('Silver iodide','Yellow'))
# 	# db.session.add(color('Silver sulphide','Black'))
# 	# db.session.add(color('Silver bromide','Yellow'))
# 	# db.session.add(color('Silver oxide','Brown'))
# 	# db.session.add(color('Hydrogen','Colorless'))
# 	# db.session.add(color('Fluorine','Colorless'))
# 	# db.session.add(color('Radium','Silver'))
# 	# db.session.add(color('Oxygen','Colorless'))
# 	# db.session.add(color('Silver','Silver' ))
# 	# db.session.add(color('Francium','Silver'))
# 	# db.session.add(color('Nitrogen','Colorless'))
# 	# db.session.add(color('Radon','Colorless'))
# 	# db.session.add(color('Palladium','Silver'))
# 	# db.session.add(color('Carbon','Black'))
# 	# db.session.add(color('Astatine'	,'Silver'))
# 	# db.session.add(color('Rhodium','Silver'))
# 	# db.session.add(color('Boron','Black'))
# 	# db.session.add(color('Polonium','Silver'))
# 	# db.session.add(color('Ruthenium','Silver'))
# 	# db.session.add(color('Beryllium','SlateGray'))
# 	# db.session.add(color('Bismuth','Gray'))
# 	# db.session.add(color('Technetium','Silver'))
# 	# db.session.add(color('Niobium','Gray'))
# 	# db.session.add(color('Neptunium','Silver'))
# 	# db.session.add(color('Aluminum','Silver' ))
# 	# db.session.add(color('Tellurium','Silver'))
# 	# db.session.add(color('Uranium','Silver'))
# 	# db.session.add(color('Magnesium','Silver'))
# 	# db.session.add(color('Protactinium','Silver'))
# 	# db.session.add(color('Antimony','Silver'))
# 	# db.session.add(color('Sodium','Silver'))
# 	# db.session.add(color( 'Thorium','Silver'))
# 	# db.session.add(color('Tin','Silver'))
# 	# db.session.add(color('Neon','Colorless'))
# 	# db.session.add(color('Actinium','Silver'))
# 	# db.session.add(color('Indium','Silver'))
# 	# db.session.add(color('Holmium','Silver'))
# 	# db.session.add(color('Cobalt','Gray'))
# 	# db.session.add(color('Nickel','Gray'))
# 	# db.session.add(color('Erbium','Silver'))
# 	# db.session.add(color('Copper','Copper'))
# 	# db.session.add(color('Dysprosium','Silver'))
# 	# db.session.add(color('Iron','Gray'))
# 	# db.session.add(color('Manganese','Silver'))
# 	# db.session.add(color('Terbium','Silver'))
# 	# db.session.add(color('Gadolinium','Silver'))
# 	# db.session.add(color('Chromium','Silver'))
# 	# db.session.add(color('Europium','Silver'))
# 	# db.session.add(color('Vanadium','Silver'))
# 	# db.session.add(color('Samarium','Silver'))
# 	# db.session.add(color('Titanium','Silver'))
# 	# db.session.add(color('Promethium','Silver'))
# 	# db.session.add(color('Scandium','Silver'))
# 	# db.session.add(color('Neodymium','Silver' 	))
# 	# db.session.add(color('Calcium','Silver'))
# 	# db.session.add(color('Praseodymium','Silver'))
# 	# db.session.add(color('Potassium','Silver'))
# 	# db.session.add(color('Lanthanum','Silver'))
# 	# db.session.add(color('Barium','Silver '))
# 	# db.session.add(color('Curium','Silver'))
# 	# db.session.add(color('Cesium','Silver'))
# 	# db.session.add(color('Americium','Silver'))
# 	# db.session.add(color( 'Plutonium','Silver'))
# 	# db.session.add(color('Silicon','Gray'))
# 	# db.session.add(color('Iodine','SlateGray'))
# 	return render_template('index1.html')

# @app.route("/main",methods=['POST','GET'])
# def he():
# 	c=[]
# 	if(request.method=='POST'):
# 		a=request.form['search']
# 		b=color.query.filter_by(rang=a).all()
# 		for i in b:
# 			c.append(i.name)
# 	return render_template('start.html',ap=c,m=a)			

from flask import render_template, request,flash, redirect, url_for,session,Flask
from app import app, db
from app.models import *
@app.route('/',methods=['GET','POST'])
def defaa():
	# db.session.add(color('Potassium dichromate','Orange'))
	# db.session.add(color('Potassium permanganate','Violet'))
	# db.session.add(color('Friferric tetraoxide','Black'))
	# db.session.add(color('Ferrous sulphate','Green'))
	# db.session.add(color('Ferric sulphate','Yellow'))
	# db.session.add(color('Ferric hydroxide','Green'))
	# db.session.add(color('Ferrous hydroxide','Orange'))
	# db.session.add(color('Ferrous chloride','Yellow'))
	# db.session.add(color('Ferric chloride','Reddish brown'))
	# db.session.add(color('Iron (II) carbonate','Brown'))
	# db.session.add(color('Iron (III) nitrate','Red'))
	# db.session.add(color('Iron (II) sulphide','Black'))
	# db.session.add(color('Iron (III) sulphide','Black'))
	# db.session.add(color('Copper carbonate','Green'))
	# db.session.add(color('Copper nitrate','Bluish green'))
	# db.session.add(color('Copper sulphate','Blue'))
	# db.session.add(color('Anhydrous copper sulphate','White'))
	# db.session.add(color('Copper sulphide','Black'))
	# db.session.add(color('Copper chloride','Yellow'))
	# db.session.add(color('Copper (II) oxide','Black'))
	# db.session.add(color('Copper (I) oxide','Red'))
	# db.session.add(color('Copper hydroxide','Blue'))
	# db.session.add(color('Red lead','Red'))
	# db.session.add(color('Lead iodide','Yellow'))
	# db.session.add(color('Lead sulphide','Black'))
	# db.session.add(color('Lead (II) oxide','Yellow'))
	# db.session.add(color('Lead (IV) oxide','Brown'))
	# db.session.add(color('Mercuric sulphide','Black'))
	# db.session.add(color('Mercuric oxide','Orange red'))
	# db.session.add(color('Silver iodide','Yellow'))
	# db.session.add(color('Silver sulphide','Black'))
	# db.session.add(color('Silver bromide','Yellow'))
	# db.session.add(color('Silver oxide','Brown'))
	# db.session.add(color('Hydrogen','Colorless'))
	# db.session.add(color('Fluorine','Colorless'))
	# db.session.add(color('Radium','Silver'))
	# db.session.add(color('Oxygen','Colorless'))
	# db.session.add(color('Silver','Silver' ))
	# db.session.add(color('Francium','Silver'))
	# db.session.add(color('Nitrogen','Colorless'))
	# db.session.add(color('Radon','Colorless'))
	# db.session.add(color('Palladium','Silver'))
	# db.session.add(color('Carbon','Black'))
	# db.session.add(color('Astatine'	,'Silver'))
	# db.session.add(color('Rhodium','Silver'))
	# db.session.add(color('Boron','Black'))
	# db.session.add(color('Polonium','Silver'))
	# db.session.add(color('Ruthenium','Silver'))
	# db.session.add(color('Beryllium','SlateGray'))
	# db.session.add(color('Bismuth','Gray'))
	# db.session.add(color('Technetium','Silver'))
	# db.session.add(color('Niobium','Gray'))
	# db.session.add(color('Neptunium','Silver'))
	# db.session.add(color('Aluminum','Silver' ))
	# db.session.add(color('Tellurium','Silver'))
	# db.session.add(color('Uranium','Silver'))
	# db.session.add(color('Magnesium','Silver'))
	# db.session.add(color('Protactinium','Silver'))
	# db.session.add(color('Antimony','Silver'))
	# db.session.add(color('Sodium','Silver'))
	# db.session.add(color( 'Thorium','Silver'))
	# db.session.add(color('Tin','Silver'))
	# db.session.add(color('Neon','Colorless'))
	# db.session.add(color('Actinium','Silver'))
	# db.session.add(color('Indium','Silver'))
	# db.session.add(color('Holmium','Silver'))
	# db.session.add(color('Cobalt','Gray'))
	# db.session.add(color('Nickel','Gray'))
	# db.session.add(color('Erbium','Silver'))
	# db.session.add(color('Copper','Copper'))
	# db.session.add(color('Dysprosium','Silver'))
	# db.session.add(color('Iron','Gray'))
	# db.session.add(color('Manganese','Silver'))
	# db.session.add(color('Terbium','Silver'))
	# db.session.add(color('Gadolinium','Silver'))
	# db.session.add(color('Chromium','Silver'))
	# db.session.add(color('Europium','Silver'))
	# db.session.add(color('Vanadium','Silver'))
	# db.session.add(color('Samarium','Silver'))
	# db.session.add(color('Titanium','Silver'))
	# db.session.add(color('Promethium','Silver'))
	# db.session.add(color('Scandium','Silver'))
	# db.session.add(color('Neodymium','Silver' 	))
	# db.session.add(color('Calcium','Silver'))
	# db.session.add(color('Praseodymium','Silver'))
	# db.session.add(color('Potassium','Silver'))
	# db.session.add(color('Lanthanum','Silver'))
	# db.session.add(color('Barium','Silver '))
	# db.session.add(color('Curium','Silver'))
	# db.session.add(color('Cesium','Silver'))
	# db.session.add(color('Americium','Silver'))
	# db.session.add(color( 'Plutonium','Silver'))
	# db.session.add(color('Silicon','Gray'))
	return render_template('index1.html')
	# return 'as'

@app.route("/main",methods=['GET','POST'])
def he():
	c=[]
	a=''
	if(request.method=='POST'):
		obj = last.query.all()
		k=str(obj[-1].colo)
		a=k
		print a
		b=color.query.filter_by(rang=k).all()
		for i in b:
			c.append(i.name)
	return render_template('start.html',ap=c,m=a)			

