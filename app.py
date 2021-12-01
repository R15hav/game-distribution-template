import os
from flask import Flask, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date

basedir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)

Migrate(app,db) #Connect app to database

class game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    size=db.Column(db.Text)
    date = db.Column(db.Text)
    disc = db.Column(db.Text)
    d_url = db.Column(db.Text)
    i_url = db.Column(db.Text)

    def __init__ (self,name,size,disc,d_url,i_url):
        today = date.today()
        self.name=name
        self.size=size
        self.date=today.strftime("%d/%m/%Y")
        self.disc=disc
        self.d_url=d_url
        self.i_url=i_url
    
    def __repr__(self):
        return f'{self.name}# {self.date}# {self.disc}# {self.d_url}# {self.i_url}# {self.size}'
    




@app.route('/',methods=['GET','POST'])
def home():
    g= game.query.all()
    g_list=[str(i) for i in g]
    if request.method=='POST':
        sr=request.form['search']
        matched_indexes = []
        i = 0
        length = len(g_list)
        sr=request.form['search']
        while i < length:
            if sr.lower() in g_list[i].lower():
                matched_indexes.append(g_list[i])
            i += 1
        if len(matched_indexes)==0:
            return render_template("index.html",games=g_list)
        else:
            return render_template("index.html",games=matched_indexes)
    else:
        return render_template("index.html",games=[str(i) for i in g])

    

if __name__ == "__main__":
    app.run(debug=False)