# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), primary_key=False)
    director = db.Column(db.String(255), primary_key=False)
    rating = db.Column(db.Integer, primary_key=False)
