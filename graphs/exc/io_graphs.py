from graphs.graph_io import load_graph, save_graph, write_dot
from graphs.graph import *
with open('examples/weightedexample.gr') as f:
    G = load_graph(f)
#     v = G.vertices[0]
#     w = G.vertices[3]
#     G.add_edge(Edge(v,w))
# with open('examples/examplegraph2.gr', 'w') as f:
#     save_graph(G, f)
with open('weightedexample.dot', 'w') as f:
        write_dot(G, f, directed=True)