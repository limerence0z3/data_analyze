from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def initDB(app: Flask):
    db.init_app(app)
    
class AgeMarrige(db.Model):
    
    __tablename__ = "Age_Marrige"
    
    year = db.Column(db.Integer, primary_key=True)
    age_group = db.Column(db.String(10), primary_key=True)
    num = db.Column(db.Integer)
    
    def __init__(self, year: int, age_group: str, num: int):
        self.year = year
        self.age_group = age_group
        self.num = num
        
        
class Unmarrige(db.Model):
    
    __tablename__ = "unmarrige"
    
    year = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    
    def __init__(self, year: int, num: int):
        self.year = year
        self.num = num
        

class CPI(db.Model):
    
    __tablename__ = "CPI"
    
    year = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    
    def __init__(self, year: int, value: int):
        self.year = year
        self.value = value
        
        
class Fertility(db.Model):
    
    __tablename__ = "Fertility"
    
    year = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    
    def __init__(self, year: int, value: int):
        self.year = year
        self.value = value
