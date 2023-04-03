class Vertex:
    def __init__(self, key):
        self.id = key         
        self.connectedTo = {}

        self.distance = 0
        self.pred = None
        self.color = "white"

        self.discovery = 0
        self.finish = 0

    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight


    def __str__(self):
        return f'{str(self.id)} connectedTo: {[x.id for x in self.connectedTo]}'


    def getConnections(self):
        return self.connectedTo.keys()


    def getId(self):
        return self.id


    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    
    def getDistance(self):
        return self.distance


    def getPred(self):
        return self.pred


    def getColor(self):
        return self.color


    def setDistance(self, distance: int):
        self.distance = distance


    def setPred(self, pred ):
        self.pred = pred


    def setColor(self, color: str):
        self.color = color


    def getDiscovery(self):
        return self.discovery


    def getFinish(self):
        return self.finish


    def setDiscovery(self, discovery):
        self.discovery = discovery


    def setFinish(self, finish):
        self.finish = finish

