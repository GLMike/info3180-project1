from . import db
import enum
from sqlalchemy import Enum, Integer




class PropertyModel(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    numBed = db.Column(db.String(50))
    numBath = db.Column(db.String(50))
    location = db.Column(db.String(50))
    price = db.Column(db.String(50))
    pType = db.Column(db.String(50))
    desc = db.Column(db.String(300))
    pic = db.Column(db.String(300))
    


    def __init__(self, title, numBed, numBath, location, price, pType, desc, pic):

        self.title = title
        self.numBed = numBed
        self.numBath = numBath
        self.location = location
        self.price = price
        self.pType = pType
        self.desc = desc
        self.pic = pic
