from datetime import datetime
from portfolio import db

class Admin(db.Model):
    admin_id= db.Column(db.Integer, autoincrement=True,primary_key=True)
    admin_name = db.Column(db.String(50),nullable=False)
    admin_loginid = db.Column(db.Integer,nullable=False)
    admin_pwd=db.Column(db.String(155),nullable=False)


class User(db.Model):
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True) 
    user_name = db.Column(db.String(45),nullable=False)
    user_email = db.Column(db.String(150),nullable=False) 
    user_message = db.Column(db.Text(),nullable=False) 
    user_date = db.Column(db.DateTime(), default=datetime.utcnow)