# app.py

from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import random
import string
from datetime import datetime

app = Flask(__name__)

# Configure the SQLAlchemy database URI to use SQLite and specify the database file as 'example.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

# Create an instance of the SQLAlchemy class and associate it with the Flask application
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)

    first_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)

    address = db.Column(db.String(255), nullable=False)
    telephone_number = db.Column(db.String(20), nullable=False)
    country_code = db.Column(db.String(5), nullable=False)
    post_code = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    date_of_birth = db.Column(db.Date, nullable=False)  
    is_active = db.Column(db.Boolean, default=True)  
    registration_date = db.Column(db.DateTime, default=db.func.current_timestamp())  

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        # Generate a random username 
        self.generate_username()
        # Generate a random password
        self.generate_password()

    def generate_username(self):
        # Generate a random username of 12 digits
        self.username = ''.join(random.choices(string.digits, k=12))

    def generate_password(self):
        # Generate a random password of 10 characters consisting of letters and digits
        password_characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(password_characters) for _ in range(10))
        # Hash the password
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Check if the provided password matches the stored hashed password
        return check_password_hash(self.password_hash, password)

    def serialize(self):  # Serialization method for jsonify
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'surname': self.surname,
            'address': self.address,
            'telephone_number': self.telephone_number,
            'country_code': self.country_code,
            'post_code': self.post_code,
            'email': self.email,
            'date_of_birth': str(self.date_of_birth),
            'is_active': self.is_active,
            'registration_date': str(self.registration_date)
        }



class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0 , nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Establishing a relationship between the Account adn User Models - reverse relationship from User back to Account
    user = db.relationship('User', backref=db.backref('accounts', lazy=True))
    
    account_type = db.Column(db.String(20), nullable=False)
    currency = db.Column(db.String(3), default='USD')
    
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  
    last_updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())  

    credit = db.Column(db.Float, default=0.0)
    debit = db.Column(db.Float, default=0.0)   

    def serialize(self):
        return {
            'id': self.id,
            'account_number': self.account_number,
            'balance': self.balance,
            'user_id': self.user_id,
            'account_type': self.account_type,
            'currency': self.currency,
            'is_active': self.is_active,
            'created_at': str(self.created_at),
            'last_updated_at': str(self.last_updated_at),
            'credit': self.credit,
            'debit': self.debit
        }


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Source account details
    source_account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    source_account = db.relationship('Account', foreign_keys=[source_account_id], backref=db.backref('outgoing_transactions', lazy=True))

    # Destination account details
    destination_account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    destination_account = db.relationship('Account', foreign_keys=[destination_account_id], backref=db.backref('incoming_transactions', lazy=True))

    transaction_type = db.Column(db.String(20), nullable=False) # Debit or Credit
    description = db.Column(db.String(255), nullable=True)



# Create tables within the application context
with app.app_context():
    db.create_all()



@app.route('/')
def hello():
    return jsonify(message="Hello, welcome to my Flask API!")



@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users=[user.serialize() for user in users])



@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json# Convert date_of_birth string to a Python date object
    date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
    new_user = User(
        first_name=data['first_name'],
        surname=data['surname'],
        address=data['address'],
        telephone_number=data['telephone_number'],
        country_code=data['country_code'],
        post_code=data['post_code'],
        email=data['email'],
        date_of_birth=date_of_birth
    )
    # Additional logic such as validating data and error handling can be added here
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User created successfully"), 201



@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    
    user = User.query.get(user_id)
    if not user:
        return jsonify(message="User not found"), 404
    
    user.first_name = data.get('first_name', user.first_name)
    user.surname = data.get('surname', user.surname)
    user.address = data.get('address', user.address)
    user.telephone_number = data.get('telephone_number', user.telephone_number)
    user.post_code = data.get('post_code', user.post_code)
    user.email = data.get('email', user.email)
    
    # Convert date_of_birth string to datetime object
    date_of_birth_str = data.get('date_of_birth')
    if date_of_birth_str:
        user.date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
    
    # Additional logic such as validating data and error handling can be added here
    
    db.session.commit()
    
    return jsonify(message="User updated successfully")



@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(error="User not found"), 404
    # Additional logic such as checking for associated data and error handling can be added here
    db.session.delete(user)
    db.session.commit()
    return jsonify(message="User deleted successfully")



@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.json
    user_id = data.get('user_id')
    account_type = data.get('account_type')  # Extracting account_type from JSON data
    user = User.query.get(user_id)
    
    if user:
        account_number = generate_account_number()  # Function to generate account number
        
        new_account = Account(
            account_number=account_number,
            user_id=user.id,
            account_type=account_type,
            balance=0.0,  # Initial balance
            currency='USD',  # Default currency
            is_active=True,  # Set account as active by default
        )
        
        db.session.add(new_account)
        db.session.commit()
        
        return jsonify(message="Account created successfully"), 201
    else:
        return jsonify(error="User not found"), 404

def generate_account_number():
    # Generate a random account number of 10 digits
    return ''.join(random.choices(string.digits, k=10))



@app.route('/delete_account/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    account = Account.query.get(account_id)
    if account:
        db.session.delete(account)
        db.session.commit()
        return jsonify(message="Account deleted successfully"), 200
    else:
        return jsonify(error="Account not found"), 404



@app.route('/get_accounts/<int:user_id>', methods=['GET'])
def get_accounts(user_id):
    user = User.query.get(user_id)
    if user:
        accounts = user.accounts
        serialized_accounts = [account.serialize() for account in accounts]
        return jsonify(accounts=serialized_accounts), 200
    else:
        return jsonify(error="User not found"), 404
    
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

