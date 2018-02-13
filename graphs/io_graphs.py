from graphs.graph_io import load_graph, save_graph
from graphs.graph import *
with open('examples/examplegraph.gr') as f:
    G = load_graph(f)
    v = list(G.vertices)[0]
    w = list(G.vertices)[3]
    G.add_edge(Edge(v,w))
with open('examples/examplegraph2.gr', 'w') as f:
    save_graph(G, f)
