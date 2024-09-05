from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False, unique=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), unique=False, nullable=False)
    store = db.relationship("StoreModel", back_populates="items")
    
    
class StoreModel(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)   
    item = db.relationship('Item', back_populates="store", lazy="dynamic")
