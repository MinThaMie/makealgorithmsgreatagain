from graphs.graph import *
# A function which creates a graph with n vertices, with a path of length n − 1;
def graph_path(n):
    G = Graph(False, n)
    verts = G.vertices
    v = verts.pop()
    while len(verts) > 0:
        w = verts.pop()
        f = Edge(v, w)
        v = w
        G.add_edge(f)
    print(G)
    return G
graph_path(2)
graph_path(6)
# A function which creates a graph with n vertices, with a cycle of length n;
def cycle_graph(n):
    G = Graph(False, n)
    verts = G.vertices
    s = verts.pop()
    l = s
    v = s
    while len(verts) > 0:
        w = verts.pop()
        f = Edge(v, w)
        l = w
        v = w
        G.add_edge(f)
    le = Edge(s,l)
    G.add_edge(le)
    print(G)
    return G
cycle_graph(4)
# A function which creates a complete graph with n vertices;
def complete_graph(n):
    G = Graph(False, n)
    verts = G.vertices
    while len(verts) > 0:
        v = verts.pop()
        for i in verts:
            f = Edge(v, i)
            G.add_edge(f)
    print(G)
    return G
complete_graph(4)

G = graph_path(5)
G2 = cycle_graph(3)
print( G + G2)


