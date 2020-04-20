import datetime as dt

from .. import db

class Card(db.Model):
    __searchable__ = ['descr']
    id        = db.Column(db.Integer, primary_key=True)
    title     = db.Column(db.String(100))
    body      = db.Column(db.String(1000))
    image     = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, index=True, default=dt.datetime.utcnow)
    user_id   = db.Column(db.Integer, db.ForeignKey('users.id'))
    language  = db.Column(db.String(5))

    def __repr__(self):
        return '<Card {}>'.format(self.title)

