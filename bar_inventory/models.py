from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime


from werkzeug.security import generate_password_hash, check_password_hash

import secrets

from flask_login import UserMixin, LoginManager

from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default= '')
    last_name = db.Column(db.String(150), nullable = True, default= '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(150), nullable = True, default= '')
    username = db.Column(db.String(150), nullable = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    # add relationship later
    
    def __init__(self, email, username, first_name = '', last_name = '', id = '', password = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.username = username
        self.token = self.set_token(24)
        
    def set_token(self, length):
        return secrets.token_hex(length)
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f"User {self.email} has been added to the database!"
    
class Bar(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Numeric(precision=10, scale=2))
    chocolate_quality = db.Column(db.String(150), nullable=True)
    melt_temp = db.Column(db.String(100), nullable=True)
    freeze_time = db.Column(db.String(100))
    dimension = db.Column(db.String(100))
    weight = db.Column(db.String(100))
    cost_of_production = db.Column(db.Numeric(precision=10, scale=2))
    series = db.Column(db.String(150))
    random_joke = db.Column(db.String, nullable=True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)

    def __init__(self, name, description, price, chocolate_quality, melt_temp, freeze_time, dimensions, weight, cost_of_production, series, random_joke, user_token):
        self.id = self.set_id()
        self.name = name
        self.description = description
        self.price = price
        self.chocolate_quality = chocolate_quality
        self.melt_temp = melt_temp
        self.freeze_time = freeze_time
        self.dimensions = dimensions
        self.weight = weight
        self.cost_of_production = cost_of_production
        self.series = series
        self.random_joke = random_joke
        self.user_token = user_token

    def set_id(self):
        return str(uuid.uuid4())

    def __repr__(self):
        return f"Bar {self.name} has been added to the database!"



class BarSchema(ma.Schema): 
    class Meta:
        fields = ['id', 'name', 'description', 'price', 'chocolate_quality', 'melt_temp', 
                  'freeze_time', 'dimensions','weight','cost_of_production','series','random_joke']

bar_schema = BarSchema()
bars_schema = BarSchema(many = True)