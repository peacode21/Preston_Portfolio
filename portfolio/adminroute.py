import os,random,string,requests

from io import BytesIO

import json

import base64

import sqlite3

import imghdr

from flask import render_template,request,session,flash,redirect,url_for,send_file,jsonify

from portfolio import app,db

from portfolio.models import Admin,User

from datetime import datetime


@app.route('/admin/dashboard')
def admin_home():
    if session.get('admin') != None:
        users = User.query.all()
        current_time = datetime.utcnow()
        return render_template('admin/index.html',users=users,current_time=current_time)
    else:
        return render_template('admin/admin_login.html')




@app.route('/admin/login',methods=['GET','POST'])
def admin_login():
    if request.method =='GET':
        return redirect(url_for('admin_form'))
    else:
        loginid = request.form.get('loginid')
        pwd = request.form.get('pwd')
        logs = db.session.query(Admin).filter(Admin.admin_loginid == loginid).first()
        if loginid !='' and pwd !='':
            if logs != None:
                chk = db.session.query(Admin).filter(Admin.admin_loginid == loginid).filter(Admin.admin_pwd == pwd).first()
                if chk != None:
                    id = logs.admin_id
                    session['admin']=id
                    db.session.commit()
                    return redirect(url_for('admin_home'))
                else:
                    flash("Invalid Credentials")
                    return redirect(url_for('admin_form'))
            else:
                flash("Invalid Credentials")
                return redirect(url_for('admin_form'))
        else:
            flash("One or more fields are empty, Please complete the form")
            return redirect(url_for('admin_form'))   



@app.route('/admin_form')
def admin_form():
    return render_template('admin/admin_login.html')





@app.route('/admin/logout/')
def admin_logout():
    if session.get('admin')!=None:
        session.pop('admin',None)
    return redirect(url_for("admin_form"))





@app.errorhandler(404)
def page404(error):
    return render_template("admin/404.html",error=error), 404



@app.errorhandler(500)
def internalerror(error):
    return render_template("admin/404.html",error=error), 500