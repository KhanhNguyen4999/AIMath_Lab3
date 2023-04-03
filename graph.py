from inspect import stack
from pickle import FALSE
from vertex import Vertex
from typing import Any, Text, List
from copy import deepcopy

from queue import Queue


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.stack = []
        self.time = 0


    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

        return newVertex


    def getVertex(self, n):
        return self.vertList[n] if n in self.vertList else None


    def __contains__(self,n):
        return n in self.vertList


    def addEdge(self, f: Any, t: Any, weight: int =0):
        if f not in self.vertList:
            nv = self.addVertex(f)

        if t not in self.vertList:
            nv = self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], weight)


    def getVertices(self):
        return self.vertList.keys()


    def __iter__(self):
        return iter(self.vertList.values())


    def bfs(self, start: Vertex):
        start.setDistance(0)
        start.setPred(None)

        vertQueue = Queue()
        vertQueue.put(start)

        while vertQueue.qsize() > 0:
            currentVert = vertQueue.get()

            for nbr in currentVert.getConnections():
                if nbr.getColor() == 'white':
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPred(currentVert)

                    vertQueue.put(nbr)


            currentVert.setColor('black')


    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(None)

        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)
    

    def dfsvisit(self, startVertex, scc = None):
        if scc is not None:
            scc.append(startVertex.getId())
        
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)

        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex, scc = scc)

        self.stack.append(startVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)


    def traverse_dfs(self):
        for vertex in self:
            key = vertex.getId()
            pred = 'None' if vertex.getPred() is None else vertex.getPred().getId()
            discovery = vertex.getDiscovery()
            finish = vertex.getFinish()

            print("key: {}, pred: {}, discovery: {}, finish: {}".format(key, pred, discovery, finish))


    def traverse_bfs(self):
        for vertex in self:
            key = vertex.getId()
            pred = 'None' if vertex.getPred() is None else vertex.getPred().getId()
            distance = vertex.getDistance()

            print("key: {}, pred: {}, distance: {}".format(key, pred, distance))

    def transpose_graph(self):
        g = Graph()

        for v in self.vertList.values():
            for w in v.getConnections():
                src = v.getId()
                tgt = w.getId()
                g.addEdge(tgt, src)
        return g
                


    def get_SCC(self):
        # Step 1: Create a stack
        self.dfs()

        # Step 2: Create transpose graph
        g_tran = self.transpose_graph()

        # Step 3: DFS and print SCC
        new_stack = [g_tran.vertList[v.getId()] for v in self.stack]
        res = []
        while new_stack:
            s = new_stack.pop(-1)
            if s.getColor() == "white":
                scc = []
                g_tran.dfsvisit(s, scc)
                res.append(scc)
        return res


def traverse(y: Vertex):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


if __name__ == '__main__':
    g = Graph()

    # Create vertex
    for i in range(5):
        g.addVertex(i)
    
    # Create edge
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(3, 4)

    print("GRAPH: ")
    for v in g:
        for w in v.getConnections():
            print(f"( {v.getId()} , {w.getId()} )")

    # Get group scc
    print("GROUP SCC:")
    group_scc = g.get_SCC()
    print(group_scc)