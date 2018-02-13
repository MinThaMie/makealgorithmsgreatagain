from graphs.graph_io import load_graph, save_graph, write_dot
from graphs.graph import *
with open('examples/examplegraph.gr') as f:
    G = load_graph(f)
    print(G)
    verts = G.vertices
    CG = Graph(False, 0)
    while len(verts) > 0:
        v = verts.pop()
        for i in verts:
            if not v.is_adjacent(i):
                nv = v
                nv._graph = CG
                ni = i
                ni._graph = CG
                f = Edge(nv, ni)
                CG.add_edge(f)
    print(CG)
with open('examples/complementgraph.gr', 'w') as f:
    save_graph(CG, f)

with open('mygraph.dot', 'w') as f:
    write_dot(G, f)