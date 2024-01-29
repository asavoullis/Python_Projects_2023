from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date
import os

# Ensure 'instance' directory exists before removing it
if os.path.exists("instance"):
    import shutil 
    shutil.rmtree("instance")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Owner(db.Model):
    """
    Represents an owner in the database.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile = db.Column(db.Integer, unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)  
    date_joined = db.Column(db.Date, default=datetime.utcnow())

    # Establish one-to-many relationship with pets
    pets = db.relationship('Pet', backref='owner')

    def __repr__(self):
        return f'<Owner(id={self.id}, name={self.name}, address={self.address}, email={self.email}, mobile={self.mobile}, date_of_birth={self.date_of_birth}, date_joined={self.date_joined})>'



class Pet(db.Model):
    """
    Represents a pet in the database.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.Integer)
    owned_id = db.Column(db.Integer, db.ForeignKey('owner.id'))

    def __repr__(self):
        return f'<Pet(id={self.id}, name={self.name}, age={self.age}, owner={self.owner.name}, owner_id={self.owned_id})>'


owners = [
    Owner(name='John Doe', address='123 Main St', email='john@example.com', mobile=1234567890, date_of_birth=datetime(1980, 1, 1)),
    Owner(name='Jane Smith', address='456 Elm St', email='jane@example.com', mobile=9876543210, date_of_birth=datetime(1975, 5, 15)),
    Owner(name='Alice Johnson', address='789 Oak St', email='alice@example.com', mobile=5555555555, date_of_birth=datetime(1990, 6, 20)),
    Owner(name='Bob Brown', address='101 Pine St', email='bob@example.com', mobile=7777777777, date_of_birth=datetime(1985, 10, 10))
]


pets = [
    Pet(name='Fluffy', age=3, owner=owners[0]),
    Pet(name='Spot', age=5, owner=owners[1]),
    Pet(name='Buddy', age=2, owner=owners[0]),
    Pet(name='Max', age=4, owner=owners[2]),
    Pet(name='Mittens', age=1, owner=owners[3]),
    Pet(name='Rocky', age=6, owner=owners[2])
]


owner1 = Owner(name='Jack Kel', address='454 Main St', email='jk@example.com', mobile=2234567890, date_of_birth=datetime(1980, 1, 1))
pet1 = Pet(name='Maxxy', age=3, owner=owner1)


def create_and_add_data():
    """
    Creates tables and adds initial data to the database.
    """
    with app.app_context():
        db.create_all()

        db.session.add_all(owners)
        db.session.add_all(pets)
        db.session.add_all([owner1, pet1])

        db.session.commit()


def print_pet_owners():
    """
    Prints pets and their owners from the database.
    """
    with app.app_context():
        print("Pets and their Owners:")
        for pet in Pet.query.all():
            print(f"Pet: {pet.name}, Age: {pet.age}, Owner: {pet.owner.name}")

def print_database_entries():
    """
    Prints entries in the 'Owner' and 'Pet' tables.
    """
    with app.app_context():
        print("\nPrinting entries in the 'Owner' table:")
        for owner in Owner.query.all():
            print(owner)
        
        print("\nPrinting entries in the 'Pet' table:")
        for pet in Pet.query.all():
            print(pet)

def print_database_entries_old():
    """
    Prints entries in the 'Owner' and 'Pet' tables.
    """
    with app.app_context():
        print("\nPrinting entries in the database:")
        print(Owner.query.all())
        print(Pet.query.all())



create_and_add_data()
print_pet_owners()
print_database_entries()
print_database_entries_old()