from flask import Flask
from flask_scpipript import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from intsance.config import app_config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config['development'])

db = SQLAlchemy()
db.init_app(app)
mongo = PyMongo(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


class Individual_EC(db.Model):
    __tablename__ = 'individual_EC'
    __bindkey__ = 'postgres_bind'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    location = db.Column(db.String(80))
    next_of_kin = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, username, location, next_of_kin, age):
        self.username = username
        self.location = location
        self.next_of_kin = next_of_kin
        self.age = age

    def __repr__(self):
        return '<Name: {} {}>'.format(self.username, self.next_of_kin)


class Individual_GIS(db.Model):
    __tablename__ = 'individual_GIS'
    __bind_key__ = 'mysql_bind'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    location = db.Column(db.String(80))
    next_of_kin = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, username, location, next_of_kin, age):
        self.username = username
        self.location = location
        self.next_of_kin = next_of_kin
        self.age = age

    def __repr__(self):
        return '<Name: {} {}>'.format(self.username, self.next_of_kin)


class Individual_NHIA(db.Model):
    __tablename__ = 'individual_NHIS'
    __bind_key__ = 'sqlite_bind'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    location = db.Column(db.String(80))
    next_of_kin = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, username, location, next_of_kin, age):
        self.username = username
        self.location = location
        self.next_of_kin = next_of_kin
        self.age = age

    def __repr__(self):
        return '<Name: {} {}>'.format(self.username, self.next_of_kin)


if __name__ == '__main__':
    manager.run()
