import util
from client import Client

class Room:
    def __init__(self, code):
        self.room_code = code
        self.fileDict = {}
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
    	#self.files = listFiles()
