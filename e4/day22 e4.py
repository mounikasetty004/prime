###adjacency mtarix

class Graph:
    def __init__(self,no_of_nodes,directed=True):
        self.no_of_nodes=no_of_nodes
        self.directed=directed
        self.list={i:set() for i in range(self.no_of_nodes)}
    def add_edge(self,node1,node2,weight=0):
        self.list[node1].add((node2,weight))
        if not self.directed:
            self.list[node2].add((node1,weight))
    def print(self):
        for i in self.list:
            print(self.list[i])
a=int(input("n:"))
g=Graph(a)
l=int(input("no:"))
for i in range(l):
    node1=int(input("n1"))
    node2=int(input("n2"))
    weight=int(input("w"))
    g.add_edge(node1,node2,weight)
g.print()
