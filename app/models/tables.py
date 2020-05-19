from app import db


class User(db.model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.name


class Result(db.Model):
    __tablename__ = "results"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    r = db.Column(db.DECIMAL(2))
    i = db.Column(db.DECIMAL(2))
    a = db.Column(db.DECIMAL(2))
    s = db.Column(db.DECIMAL(2))
    e = db.Column(db.DECIMAL(2))
    c = db.Column(db.DECIMAL(2))

    user = db.relationship('User', foreign_keys=id_user)

    def __init__(self, id_user, r, i, a, s, e, c):
        self.id_user = id_user
        self.r = r
        self.i = i
        self.a = a
        self.s = s
        self.e = e
        self.c = c

    def __repr__(self):
        return "<Result %r>" % self.id
