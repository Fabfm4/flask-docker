from datetime import datetime

from firstapp import db, bcrypt


class TimeStampedMixin(object):

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)


class CatalogueMixin(TimeStampedMixin):

    name = db.Column(db.String(600), nullable=False)
    is_active = db.Column(db.Boolean())


class UserMixin(CatalogueMixin):

    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=True)
    login_with_password = True

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password, 12)

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
