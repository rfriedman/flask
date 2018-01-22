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

