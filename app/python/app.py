#!flask/bin/python
from flask import Flask, jsonify, request, redirect

app = Flask(__name__)
users = list()
record = {"usrid":"1198","usrname":"rfriedman"}
users.append(record)

@app.route('/login', methods=['GET','POST'])
def login():
      direct = redirect('http://google.com')
      if request.form['usrid']:
       usrid = request.form['usrid']
       for u in users:
        if u['usrid'] == usrid:
          direct = redirect('/index')
      return direct

@app.route('/index', methods=['GET'])
def index():
    return redirect('http://google.com') 
    

if __name__ == '__main__':

 app.run(debug=True)


