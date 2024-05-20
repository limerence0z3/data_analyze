from sqlalchemy import Column, Integer, String, Float, create_engine
from os import environ
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(environ["SQLALCHEMY_DATABASE_URI"])
db = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class AgeMarrige(db):
    
    __tablename__ = "age_marrige"
    
    year = Column(Integer, primary_key=True)
    age_group = Column(String(10), primary_key=True)
    num = Column(Integer)
    
    def __init__(self, year: int, age_group: str, num: int):
        self.year = year
        self.age_group = age_group
        self.num = num
        
        
class Unmarrige(db):
    
    __tablename__ = "unmarrige"
    
    year = Column(Integer, primary_key=True)
    num = Column(Integer)
    
    def __init__(self, year: int, num: int):
        self.year = year
        self.num = num
        

class CPI(db):
    
    __tablename__ = "cpi"
    
    year = Column(Integer, primary_key=True)
    value = Column(Float)
    
    def __init__(self, year: int, value: int):
        self.year = year
        self.value = value
        
        
class Fertility(db):
    
    __tablename__ = "fertility"
    
    year = Column(Integer, primary_key=True)
    value = Column(Integer)
    
    def __init__(self, year: int, value: int):
        self.year = year
        self.value = value

def initDB():
    db.metadata.create_all(engine)