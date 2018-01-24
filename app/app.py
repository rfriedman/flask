#!flask/bin/python
from flask import Flask, jsonify, request, redirect, render_template

app = Flask(__name__)
users = list()
record = {"usrid":"1198","usrname":"rfriedman"}
session = list()
users.append(record)

@app.route('/login', methods=['GET','POST'])
def login():
      if request.form['usrid']:
       usrid = request.form['usrid']
       for u in users:
        if u['usrid'] == usrid:
           record={"sessionid":usrid,"usrid":usrid}
           session.append(record)
      return record

@app.route('/index', methods=['GET'])
def index(name=None):
    return render_template('index.html') 
    

if __name__ == '__main__':

 app.run(debug=True)


