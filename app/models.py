from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    task_description = db.Column(db.String(256), index=True)
    due_date = db.Column(db.DateTime, nullable= True)
    created_by = db.Column(db.String(128), nullable= False)
    status = db.Column(db.Boolean)
    deleted_by = db.Column(db.String(128), nullable= True)
    created_at = db.Column(db.DateTime, nullable= True)
    deleted_at = db.Column(db.DateTime, nullable= True)

    def __init__(self, task_description, due_date, created_by, status, deleted_by, created_at, deleted_at):
        self.task_description = task_description
        self.due_date = due_date
        self.created_by = created_by
        self.status = status
        self.deleted_by = deleted_by
        self.created_at = created_at
        self.deleted = deleted_at


    def __repr__(self):
        return '<Task {}>'.format(self.task_description)



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

