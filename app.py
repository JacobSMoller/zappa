from flask import Flask, render_template
from core import db, Match, Team, Map
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

pg_url = f'postgresql://{username}:{password}@{db_url}/'
app.config['SQLALCHEMY_DATABASE_URI'] = pg_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db.init_app(app)


@app.route('/<int:hltv_id>')
def match_stats(hltv_id):
    match = Match.query.filter_by(hltv_id=hltv_id).first()
    team_a = Team.query.filter_by(id=match.team_a_id).first()
    team_b = Team.query.filter_by(id=match.team_b_id).first()
    best_of = match.bestof
    print(match.id)
    match_maps = Map.query.filter_by(match_id=match.id).all()
    maps = []
    for match_map in match_maps:
        maps.append(match_map.map)
        map_string = ', '.join(maps)

    return render_template('hello.html', team_a_name=team_a.name,
                           team_b_name=team_b.name, best_of=best_of,
                           match_map=map_string)


if __name__ == "__main__":
    app.run()
