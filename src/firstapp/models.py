from firstapp import db
from firstapp.core.db.models import UserMixin


class User(UserMixin, db.Model):
    pass
