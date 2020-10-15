
import sys


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        for node in range(self.V):
            if (dist[node] == 2147483647):
                dist[node] = -1
            print(dist[node])

    def minDistance(self, dist, sptSet):

        min = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and \
                        sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


initInput = list(map(int, input().strip().split()))
length = initInput[0]
lines = initInput[1]
source = initInput[2]

graphList=[]
for i in range(0, length):
    graphList.append([0]*length)


for i in range(0, lines):
    lineInput = list(map(int, input().strip().split()))
    a = lineInput[0] - 1
    b = lineInput[1] - 1
    graphList[a][b] = lineInput[2]

g = Graph(length)
g.graph = graphList

g.dijkstra(source-1);
