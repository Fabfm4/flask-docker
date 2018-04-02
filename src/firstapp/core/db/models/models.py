from firstapp import db
from datetime import datetime


class TimeStampedMixin(object):

    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)


class CatalogueMixin(TimeStampedMixin):

    name = db.Column(db.String(600), nullable=False)
    is_active = db.Column(db.Boolean())
