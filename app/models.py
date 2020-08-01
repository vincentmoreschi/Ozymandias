from flask_sqlalchemy import SQLAlchemy
from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),unique=True, index=True)



class MapData(db.Model):
    __tablename__ = 'map'
    uuid = db.Column(db.String, primary_key=True)
    #image_file = db.Column(db.String,unique=True, index=True)
