from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date

import os
import shutil 

if os.path.exists("instance"):
    shutil.rmtree("instance")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)  
    date_joined = db.Column(db.Date, default=datetime.utcnow())


    def __repr__(self):
        return f'<User: {self.username} {self.email}>'


anthony = User(username='Anthony', email='anthony@gmail.com', date_of_birth=datetime(1990, 1, 1))  
sarah = User(username='Sarah', email='sarah@gmail.com', date_of_birth=datetime(1995, 5, 10))  
jack = User(username='Jack', email='jack@gmail.com', date_of_birth=datetime(1990, 2, 15))  

users = [
    User(username='John', email='john@example.com', date_of_birth=datetime(1985, 5, 15)),
    User(username='Emma', email='emma@example.com', date_of_birth=datetime(1992, 9, 23)),
    User(username='Michael', email='michael@example.com', date_of_birth=datetime(1980, 3, 8)),
    User(username='Sophia', email='sophia@example.com', date_of_birth=datetime(1998, 11, 20)),
    User(username='William', email='william@example.com', date_of_birth=datetime(1975, 7, 12)),
    User(username='Olivia', email='olivia@example.com', date_of_birth=datetime(2000, 2, 28))
]


with app.app_context():
    print("\nBefore adding any users in the database:")
    db.create_all()
    print(User.query.all())

with app.app_context():
    print("\nAdding Anthony and Sarah:")
    db.session.add(anthony)
    db.session.add(sarah)
    db.session.add(jack)
    db.session.commit()
    print(User.query.all())

    print("\nQuerying the database:")
    print(User.query.filter_by(username='Anthony').first())

    print("\nUpdating anthony's email:")
    anthony.email = 'anthony@yahoo.com'
    db.session.commit()
    print(User.query.all())

    print("\nDeleting user Jack")
    db.session.delete(jack)
    db.session.commit()
    print("count of users:", User.query.count())
    print(User.query.filter_by(username='Jack').count())
    print(User.query.filter_by(username='Jack').all())
    print(User.query.all())

    print("\nAdding the rest of the Users:")
    db.session.add_all(users)
    db.session.commit()
    print(User.query.all())
    print("Getting the users that joined after Jan 1st of 2021:")
    print(User.query.filter(User.date_joined > date(2021, 1, 1)).count())

