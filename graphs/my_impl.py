from graphs.mygraph import *

G = Graph(False, 5)
e = Edge(G.vertices[0], G.vertices[1])
e2 = Edge(G.vertices[1], G.vertices[2])
G.add_edge(e)
G.add_edge(e2)
print(G)
G.del_edge(G.edges[0])
print(G)
G.add_edge(e)
print(G)
G.del_vertex(G.vertices[0])
print(G)
