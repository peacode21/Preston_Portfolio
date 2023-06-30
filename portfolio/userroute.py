import os,random,string,requests

from io import BytesIO

import json

import base64

import sqlite3

import imghdr

from flask import render_template,request,session,flash,redirect,url_for,send_file,jsonify

from sqlalchemy.sql import text

from sqlalchemy import or_

from werkzeug.security import generate_password_hash,check_password_hash

from portfolio import app,db

from portfolio.models import User

from datetime import datetime

@app.route('/')
def home():
    return render_template('user/index.html')



@app.route('/send/message',methods=['GET','POST'])
def contact_form():
    if request.method =='GET':
        return redirect(url_for('home'))
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        if name == '' or email == '' or message == '':
            flash('One or more fields are empty, please complete the form')
            return redirect(url_for('home'))
        else:
            u = User(user_name=name,user_email=email,user_message=message,)
            db.session.add(u)
            db.session.commit()
            flash('Message Sent Successfully')
            return redirect(url_for('home'))



@app.errorhandler(404)
def page404(error):
    return render_template("user/404.html",error=error), 404



@app.errorhandler(500)
def internalerror(error):
    return render_template("user/404.html",error=error), 500