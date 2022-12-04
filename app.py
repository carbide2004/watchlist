import os
import sys

from flask import Flask
from flask import render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

name = 'Carbide'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
