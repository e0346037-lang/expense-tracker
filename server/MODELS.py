from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    _tablename_ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    # This links the user to their specific expenses
    expenses = db.relationship('Expense', backref='user', lazy=True)

class Expense(db.Model, SerializerMixin):
    _tablename_ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String, nullable=False) # e.g., Food, Rent
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False