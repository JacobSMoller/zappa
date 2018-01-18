from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Match(db.Model):
    __tablename__ = 'match'
    id = db.Column(db.String, primary_key=True)
    hltv_id = db.Column(db.Integer)
    hltv_raw_dump = db.Column(db.String)
    team_a_id = db.Column(db.String)
    team_b_id = db.Column(db.String)
    date = db.Column(db.Date)
    bestof = db.Column(db.Integer)


class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)


class Map(db.Model):
    __tablename__ = 'match_map'
    id = db.Column(db.String, primary_key=True)
    map = db.Column(db.String)
    match_id = db.Column(db.String)
