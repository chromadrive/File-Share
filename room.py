import util
from client import Client

class Room:
    def __init__(self, code):
        self.room_code = code
        self.fileDict = {}
        self.fileSend = {}
        self.users = []
        #self.files = []
        """
    def listFiles(self):
    	newlst = []
    	for f in self.fileDict:
    		newlst.append(self.fileDict[f])
    	return newlst
        """

    def deleteFile(self, key):
    	if key in self.fileDict:
    		del self.fileDict[key]
    	#self.files = listFiles()

    def addFile(self, filename, sender):
    	self.fileDict[filename] = sender
        print('before')
        self.fileSend[filename] = []
        print('after')
    	#self.files = listFiles()

    def addUser(self, user):
    	self.users.append(user)

    def sendTo(self, filename, receivers):
        for afile in self.fileSend:
            if afile == filename:
                for receiver in receivers:
                    self.fileSend.setdefault(afile, []).append(receiver)
