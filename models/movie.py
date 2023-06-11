from app import db
from flask import Flask

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    poster_path = db.Column(db.String(255))
    language = db.Column(db.String(50))
    overview = db.Column(db.Text)
    release_date = db.Column(db.Date)

    def __init__(self, title, poster_path, language, overview, release_date):
        self.title = title
        self.poster_path = poster_path
        self.language = language
        self.overview = overview
        self.release_date = release_date
