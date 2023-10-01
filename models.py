from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Hero(db.model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255), nullable= False)

class Power(db.model):
    id=db.Column(db.Integer, primary_key=True)
    description=db.Column(db.String(255), nullable=False)

class HeroPower(db.model):
    id=db.Column(db.Integer, primary_key=True)
    hero_id=db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id=db.Column(db.Integer, db.ForeignKey('power.id', nullable=False))
    strength=db.Column(db.Integer, nullable=False)