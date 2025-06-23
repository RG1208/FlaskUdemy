from flask_sqlalchemy import SQLAlchemy # type: ignore
from datetime import datetime
from werkzueg.security import generate_password_hash, check_password_hash # type: ignore

db = SQLAlchemy()

member_topic_table = db.Table('member_topics',  
    db.Column('member_id', db.Integer, db.ForeignKey('member.id'), primary_key=True),
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'), primary_key=True)
)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=True)
    first_learn_date  = db.Column(db.DateTime, nullable=True)
    fav_language = db.Column(db.ForeignKey('language.id'), nullable=True)
    about = db.Column(db.Text, nullable=True)
    learn_new_interests = db.Column(db.Boolean, nullable=True)
    interest_in_topics = db.relationship('Topic', secondary=member_topic_table, backref=db.backref('members', lazy='dynamic'))

    @property
    def password(self):
        raise AttributeError("Password is not readable")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)