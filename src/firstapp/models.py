from firstapp import db
from firstapp.core.db.models import CatalogueMixin


class User(CatalogueMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
