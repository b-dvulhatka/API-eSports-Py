import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from app.player.models import Player
from app import api, db

player = Blueprint('player', __name__)

parser = reqparse.RequestParser()
parser.add_argument('Name', type=str)
parser.add_argument('nickName', type=str)
parser.add_argument('teamName', type=str)
parser.add_argument('role', type=str)
parser.add_argument('Kills', type=int)
parser.add_argument('Assists', type=int)
parser.add_argument('Deaths', type=int)
parser.add_argument('Matchs', type=int)
parser.add_argument('Wins', type=int)
parser.add_argument('kda', type=float)
parser.add_argument('winRate', type=float)

@player.route("/")
@player.route("/home")

def home():
    return "Catálogo de players de eSports"

class PlayerAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            players = Player.query.paginate(page, 10).items
        else:
            players = [Player.query.get(id)]
        if not players:
            abort(404)

        res = {}
        for plr in players:
            res[plr.id] = {
                'Name'     :  plr.playerName,
                'nickName'       :  plr.nickName,
                'teamName'       :  plr.teamName,
                'role'           :  plr.role,
                'Kills'     :  plr.Kills,
                'Assists'   :  plr.Assists,
                'Deaths'    :  plr.Deaths,
                'Matchs'    :  plr.Matchs,
                'Wins' :  plr.Wins,
                'kda'            :  str(plr.kda),
                'winRate'    :  str(plr.winRate)
            }

        return json.dumps(res)

    def post(self):
        args = parser.parse_args()

        Name     = args['Name']
        nickName       = args['nickName']
        teamName       = args['teamName']
        role           = args['role']
        Kills     = args['Kills']
        Assists   = args['Assists']
        Deaths    = args['Deaths']
        Matchs    = args['Matchs']
        Wins = args['Wins']
        kda            = (Kills + Assists) if Deaths == 0 else (Kills + Assists / Deaths)
        winRate    = ((Wins / Matchs) * 100)

        plr = Player(Name, nickName, teamName, role, Kills, Assists, Deaths, Matchs, Wins, kda, winRate)
        db.session.add(plr)
        db.session.commit()

        res = {}
        res[plr.id] = {
                'Name'     :  plr.Name,
                'nickName'       :  plr.nickName,
                'teamName'       :  plr.teamName,
                'role'           :  plr.role,
                'Kills'     :  plr.Kills,
                'Assists'   :  plr.Assists,
                'Deaths'    :  plr.Deaths,
                'Matchs'    :  plr.Matchs,
                'Wins' :  plr.Wins,
                'kda'            :  str(plr.kda),
                'winRate'    :  str(plr.winRate)
            }

        return json.dumps(res)

    def delete(self, id):
        con = Player.query.get(id)
        db.session.delete(con)
        db.session.commit()
        res = {'id' : id}
        return json.dumps(res)

    def put(self, id):
        con = Player.query.get(id)
        args = parser.parse_args()

        Name     = args['Name']
        nickName       = args['nickName']
        teamName       = args['teamName']
        role           = args['role']
        Kills     = args['Kills']
        Assists   = args['Assists']
        Deaths    = args['Deaths']
        Matchs    = args['Matchs']
        Wins = args['Wins']
        kda            = (Kills + Assists) if Deaths == 0 else (Kills + Assists / Deaths)
        winRate    = ((Wins / Matchs) * 100)

        con.Name     = Name
        con.nickName       = nickName
        con.teamName       = teamName
        con.role           = role
        con.Kills     = Kills
        con.Assists   = Assists
        con.Deaths    = Deaths
        con.Matchs    = Matchs
        con.Wins = Wins
        con.kda            = kda
        con.winRate    = winRate

        db.session.commit()

        res = {}
        res[con.id] = {
                'Name'     :  con.Name,
                'nickName'       :  con.nickName,
                'teamName'       :  con.teamName,
                'role'           :  con.role,
                'Kills'     :  con.Kills,
                'Assists'   :  con.Assists,
                'Deaths'    :  con.Deaths,
                'Matchs'    :  con.Matchs,
                'Wins' :  con.Wins,
                'kda'            :  str(con.kda),
                'winRate'    :  str(con.winRate)
            }

        return json.dumps(res)

api.add_resource(
    PlayerAPI,
    '/api/player',
    '/api/player/<int:id>',
    '/api/player/<int:id>/<int:page>'
)