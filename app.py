'''

配置格式：SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/fishballgame?charset=utf8'

DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Player(db.Model):
    __tablename__ = 'player'
    id= db.Column(db.Integer,primary_key = True,autoincrement = True)
    name = db.Column(db.String(100),nullable = False)
    content = db.Column(db.TEXT,nullable = True)

1.add 的执行：
    player = Player(name = '', content = '')
    db.seesion.add(player)
    db.seesion.commit()

2.select 的执行：
    player = Player.query.filter(‘筛选条件’).first

3.
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
db.create_all()

class Player(db.Model):
    __tablename__ = 'playertest'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    name = db.Column(db.String(5),nullable = False)
    age = db.Column(db.Integer,nullable = True,default=18)

db.create_all()

@app.route('/')
def hello_world():
    # player1 = Player(name='ws',age=5)
    # player2 = Player(name='wsc')
    # db.session.add(player1)
    # db.session.add(player2)
    # db.session.commit()
    player1 = Player.query.filter(Player.id ==1).first()
    player1.name = u'康康'
    db.session.commit()

    return player1.name

if __name__ == '__main__':
    app.run()


