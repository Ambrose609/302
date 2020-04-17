import os
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_wtf import form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
import pymysql
import cx_Oracle
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'development key'
db = pymysql.connect('localhost', 'root', '', 'amazon')
'''conn = cx_Oracle.connect('G1_team03/ceG1/@144.214.177.102/xe')'''

@app.route('/index', methods = ['POST' , 'GET'])
def index():
	return render_template('index.html')

@app.route('/amazon_login', methods = ['POST' , 'GET'])
def amazon_login():
	return render_template('amazon_login.html')

@app.route('/FedEx_login', methods = ['POST' , 'GET'])
def FedEx_login():
	return render_template('FedEx_login.html')

@app.route('/amazon_addorder', methods = ['POST' , 'GET'])
def amazon_addorder():
	return render_template('amazon_addorder.html')

@app.route('/amazonlogining', methods = ['POST' , 'GET'])
def amazonlogining():
	if request.method == 'POST':
		a1 = request.form['Amazon']
		a2 = request.form['Password']
		Amazon = 'Amazon';
		Password = 'Password';

		if a1 != Amazon or a2 != Password:
			msg = 'Wrong username or password.'
			return render_template('sent.html', msg = msg)
		else:
			return  render_template('amazon_addorder.html')

@app.route('/fedexlogining', methods = ['POST' , 'GET'])
def fedexlogining():
	if request.method == 'POST':
		a1 = request.form['FedEx']
		a2 = request.form['Password']
		FedEx = 'FedEx';
		Password = 'Password';

		if a1 != FedEx or a2 != Password:
			msg = 'Wrong username or password.'
			return render_template('sent2.html', msg = msg)
		else:
			cursor = db.cursor()
			sql = ("SELECT * FROM amazon_order ORDER BY order_id ASC")
			cursor.execute(sql)
			db.commit()
			rows = cursor.fetchall()
			print("Received the following order(s)")
			print("-----------------------------------------------------------------------")
			for row in rows:
				x = {
					"order_id": row[0],
					"sender_name":  row[1],
					"sender_address":  row[2],
					"sender_contact":  row[3],
					"receiver_name":  row[4],
					"receiver_address":  row[5],
					"receiver_contact":  row[6],
					"postal_code":  row[7]
				}
				y = json.dumps(x)
				print(y)
				print("-----------------------------------------------------------------------")
			return render_template('fedex_vieworder.html', rows = rows)

@app.route('/addorder', methods = ['POST' , 'GET'])
def addorder():
	if request.method == 'POST':
		try:
			oid = request.form['id']
			name = request.form['name']
			add = request.form['add']
			scon = request.form['scon']
			rname = request.form['rname']
			radd = request.form['radd']
			rcon = request.form['rcon']
			pos = request.form['pos']

			cursor = db.cursor()
			sql = '''
			INSERT INTO amazon_order (order_id, sender_name, sender_address, sender_contact, receiver_name, receiver_address, receiver_contact, postal_code) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')
			'''
			cursor.execute(sql%(oid,name,add,scon,rname,radd,rcon,pos) )
			
			db.commit()
						 
			x = {
			'order_id': oid,
			"sender_name": name,
			"sender_address": add,
			"sender_contact": scon,
			"receiver_name": rname,
			"receiver_address": radd,
			"receiver_contact": rcon,
			"postal_code": pos
			}

			y = json.dumps(x)
			print(y)
			print("-----------------------------------------------------------------------")
			print('Order sent')
			with open('mydata.json', 'w') as f:
				json.dump(x, f)
			msg = "You have add one order, "+"Please check the json string on console"
		except:
			db.rollback()
			msg = "Please input right value"
		finally:
			return render_template("sent3.html",msg = msg)
			db.close()

@app.route('/amazon_updateorder', methods = ['POST', 'GET']) 
def amazon_updateorder():
	cursor = db.cursor()
	sql = ("SELECT * FROM amazon_order ORDER BY order_id ASC")
	cursor.execute(sql)
	db.commit()
	rows = cursor.fetchall()
	print("Sent the following order(s)")
	print("-----------------------------------------------------------------------")
	for row in rows:
		x = {
			"order_id": row[0],
			"sender_name":  row[1],
			"sender_address":  row[2],
			"sender_contact":  row[3],
			"receiver_name":  row[4],
			"receiver_address":  row[5],
			"receiver_contact":  row[6],
			"postal_code":  row[7]
			}
		y = json.dumps(x)
		print(y)
		print("-----------------------------------------------------------------------")
	return render_template('amazon_updateorder.html', rows = rows)

@app.route('/updateorder', methods = ['POST' , 'GET'])
def updateorder():
	if request.method == 'POST':
		try:
			oid = request.form['id']
			name = request.form['name']
			add = request.form['add']
			scon = request.form['scon']
			rname = request.form['rname']
			radd = request.form['radd']
			rcon = request.form['rcon']
			pos = request.form['pos']

			cursor = db.cursor()
			sql = ("UPDATE amazon_order SET order_id = '"+oid+"', sender_name = '"+name+"', sender_address = '"+add+"', sender_contact = '"+scon+"', receiver_name = '"+rname+"', receiver_address = '"+radd+"', receiver_contact = '"+rcon+"', postal_code = '"+pos+"' WHERE order_id = '"+oid+"' ")
			
			cursor.execute(sql)
			
			db.commit()
						 
			x = {
			'order_id': oid,
			"sender_name": name,
			"sender_address": add,
			"sender_contact": scon,
			"receiver_name": rname,
			"receiver_address": radd,
			"receiver_contact": rcon,
			"postal_code": pos
			}

			y = json.dumps(x)
			print(y)
			print("-----------------------------------------------------------------------")
			print('Order updated')
			msg = "You have update one order, "+"Please check the json string on console"
		except:
			db.rollback()
			msg = "Please input right value"
		finally:
			return render_template("sent4.html",msg = msg)
			db.close()

@app.route('/fedex_vieworder', methods = ['POST', 'GET']) 
def fedex_vieworder():
	cursor = db.cursor()
	sql = ("SELECT * FROM amazon_order ORDER BY order_id ASC")
	cursor.execute(sql)
	db.commit()
	rows = cursor.fetchall()
	print("Received the following order(s)")
	print("-----------------------------------------------------------------------")
	for row in rows:
		x = {
			"order_id": row[0],
				"sender_name":  row[1],
				"sender_address":  row[2],
				"sender_contact":  row[3],
				"receiver_name":  row[4],
				"receiver_address":  row[5],
				"receiver_contact":  row[6],
				"postal_code":  row[7]
			}
		y = json.dumps(x)
		print(y)
		print("-----------------------------------------------------------------------")
	return render_template('fedex_vieworder.html', rows = rows)

@app.route('/completeorder', methods = ['POST' , 'GET'])
def completeorder():
	if request.method == 'POST':

			completeID = request.form['complete']

			cursor = db.cursor()
			sql = ("DELETE FROM amazon_order WHERE order_id = '"+completeID+"' ")
			cursor.execute(sql)
			db.commit()
			print(sql)

			msg = "success"
			return render_template("received.html",msg = msg)
			db.close()

@app.route('/cannelorder', methods = ['POST' , 'GET'])
def cannelorder():
	if request.method == 'POST':

			completeID = request.form['complete']

			cursor = db.cursor()
			sql = ("DELETE FROM amazon_order WHERE order_id = '"+completeID+"' ")
			cursor.execute(sql)
			db.commit()
			print(sql)

			msg = "success"
			return render_template("sent4.html",msg = msg)
			db.close()

@app.route('/test_amazon', methods = ['POST', 'GET']) 
def test_amazon():
	return render_template('test_amazon.html')



@app.route('/test_fedex', methods = ['POST', 'GET']) 
def test_fedex():
	cursor = con.cursor()
	sql = ("SELECT * FROM ")
	cursor.execute(sql)
	con.commit()
	rows = cursor.fetchall()

	return render_template('test_fedex.html', rows = rows)


if __name__ =='__main__':
	app.run(debug = True)

