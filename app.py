#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])

def get_tasks():
    record=dict()
    task=list()

    record['id'] = 1
    record['title'] = 'Buy groceries'
    task.append(record)
    record = dict()
    record['id'] = 2
    record['title'] = 'Learn python'
    task.append(record)

    return jsonify({'tasks': task})

if __name__ == '__main__':

 app.run(debug=True)


 def __init__(self, batchfile):
      with open(batchfile,'r') as data:
        self.batch = json.load(data)
      self.hostuser = self.batch['hostuser']
      self.clientuser = self.batch['clientuser']
      self.hostlist = self.batch['hostlist']
      self.joblist = self.batch['joblist']
      self.node = dict()
      self.proclist = list()
      self.cmds = list()

