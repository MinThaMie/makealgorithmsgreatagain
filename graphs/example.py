from graphs.graph import *
G = Graph(False, 4)
print(G)
u = Vertex(G)
print(u)
v = Vertex(G)
G.is_adjacent(u, v)
f = Edge(v, u)
G.add_edge(f)
G.is_adjacent(u, v)
print(G)
w = Vertex(G)
G.add_vertex(w)
e = Edge(u, w)
G+=e
print(e.tail)
print(e.head)
print(e.other_end(u))
print(w in G.vertices)
print(e in G.edges)
print(u.degree)
print(v in u.neighbours)
x = Vertex(G, 'X')
G+=x
print(G)
print(x)