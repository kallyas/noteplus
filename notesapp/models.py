# This file contains the models for the notesapp app
from notesapp import db
from datetime import datetime
from flask_login import UserMixin
from pytz import timezone
from sqlalchemy import event
import hashlib

_timezone = timezone('Africa/Nairobi')


class ExtraMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now(_timezone))
    updated_at = db.Column(db.DateTime, default=datetime.now(_timezone), onupdate=datetime.now(_timezone))
    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.id)



class User(UserMixin, ExtraMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    notes = db.relationship('Note', backref='author', lazy=True)
    # created_at = db.Column(db.DateTime, default=datetime.now(_timezone))
    # updated_at = db.Column(db.DateTime, default=datetime.now(_timezone), onupdate=datetime.now(_timezone))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def verify_password(password, hash):
        return hashlib.sha256(password.encode()).hexdigest() == hash

    @staticmethod
    def generate_hash(password):
        return hashlib.sha256(password.encode()).hexdigest()



class Note(db.Model, ExtraMixin):
    __tablename__ = 'notes'
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reminder_date = db.Column(db.DateTime, nullable=True)
    icon = db.Column(db.String(100), nullable=True)
    priority = db.Column(db.String(100), nullable=True, default='low')

    def __repr__(self):
        return f"Note('{self.title}', '{self.content}')"

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'reminder_date': self.reminder_date,
            'icon': self.icon,
            'priority': self.priority
        }

    @classmethod
    def get_user_notes(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def get_user_note_by_id(cls, user_id, note_id):
        return cls.query.filter_by(user_id=user_id, id=note_id).first()

    @classmethod
    def get_user_note_by_title(cls, user_id, title):
        return cls.query.filter_by(user_id=user_id, title=title).first()



class ResetPassword(db.Model, ExtraMixin):
    __tablename__ = 'reset_password'
    email = db.Column(db.String(100), nullable=False)
    token = db.Column(db.String(100), nullable=False)
    is_used = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"ResetPassword('{self.email}', '{self.token}')"

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reset_password_token(cls, token):
        return cls.query.filter_by(token=token).order_by(cls.created_at.desc()).first()

    @staticmethod
    def generate_token(email):
        return hashlib.sha256(email.encode()).hexdigest()

    @staticmethod
    def verify_token(email, token):
        return hashlib.sha256(email.encode()).hexdigest() == token