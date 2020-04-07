from app import db

class Player(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    Name     = db.Column(db.String(100))
    nickName       = db.Column(db.String(100))
    teamName       = db.Column(db.String(100))
    role           = db.Column(db.String(100))
    Kills     = db.Column(db.Integer)
    Assists   = db.Column(db.Integer)
    Deaths    = db.Column(db.Integer)
    Matchs    = db.Column(db.Integer)
    Win = db.Column(db.Integer)
    kda            = db.Column(db.Float(asdecimal=True))
    winRate    = db.Column(db.Float(asdecimal=True))

    def __init__(self,Name, nickName, teamName, role, Kills, Assists, Deaths, Matchs, totalWin, kda, winRate):
        self.Name     = Name
        self.nickName       = nickName
        self.teamName       = teamName
        self.role           = role
        self.Kills     = Kills
        self.Assists   = Assists
        self.Deaths    = Deaths
        self.Matchs    = Matchs
        self.Win = totalWin
        self.kda            = kda
        self.winRate    = winRate

    def __repr__():
        return 'Player {0}'.format(self.id)