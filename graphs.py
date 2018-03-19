from collections import defaultdict
class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


    def bfs(self,v):
        visited = [False] * len(self.graph)
        queue = []
        queue.append(v)
        while queue:
            ele = queue.pop()
            print(ele)
            for i in self.graph[ele]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)

    def DFS(self,v,visited):
        visited[v] = True
        print(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS(i,visited)

    def DFSInit(self,v):
        visited = [False]*len(self.graph)
        self.DFS(v,visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFSInit(2)
g.bfs(2)