from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import Column, Integer, String, Float
from os import environ

db = SQLAlchemy()

def initDB(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = environ["SQLALCHEMY_DATABASE_URI"]
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
class AgeMarrige(db.Model):
    
    __tablename__ = "Age_Marrige"
    
    year = Column(Integer, primary_key=True)
    age_group = Column(String(10), primary_key=True)
    num = Column(Integer)
    
    def __init__(self, year: int, age_group: str, num: int):
        self.year = year
        self.age_group = age_group
        self.num = num
        
        
class Unmarrige(db.Model):
    
    __tablename__ = "unmarrige"
    
    year = Column(Integer, primary_key=True)
    num = Column(Integer)
    
    def __init__(self, year: int, num: int):
        self.year = year
        self.num = num
        

class CPI(db.Model):
    
    __tablename__ = "CPI"
    
    year = Column(Integer, primary_key=True)
    value = Column(Float)
    
    def __init__(self, year: int, value: int):
        self.year = year
        self.value = value
        
        
class Fertility(db.Model):
    
    __tablename__ = "Fertility"
    
    year = Column(Integer, primary_key=True)
    value = Column(Integer)
    
    def __init__(self, year: int, value: int):
        self.year = year
        self.value = value
