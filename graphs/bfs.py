from graphs.graph_io import load_graph, save_graph, write_dot

def breath_first_search(s):
    L = list()
    L.append(s)
    k = 1
    label = {s: 1}
    s.label = 1
    pred = {s: []}
    while not len(L) == 0:
        v = L.pop(0)
        neighs = v.neighbours
        for n in neighs:
            if not n in label:
                k = k + 1
                label[n] = k
                n.label = k
                pred[n] = [v] + pred[v]
                L.append(n)
    return label,pred

def depth_first_search(s):
    L = list()
    L.append(s)
    k = 1
    label = {}
    pred = {s: []}
    while not len(L) == 0:
        v = L.pop()
        if not v in label:
            label[v] = k
            k = k + 1
            for n in v.neighbours:
                if n not in label :
                    pred[n] = [v] + pred[v]
                    L.append(n)
    return label,pred

def is_connected(labels, vertices):
    return len(labels) == len(vertices)

def distances(preds):
    dist = {}
    for p, v in preds.items():
        dist[p] = len(v)
    return dist

with open('examples/bfs-dfs.gr') as f:
    G = load_graph(f)
    s = G.vertices[0]
    print(G)
    labels, preds =  breath_first_search(s)
    print("bfs labels: ", labels)
    print("bfs preds: ", preds)
    print("bfs distances: ", distances(preds))
    print("G is connected: ", is_connected(labels, G.vertices))
    print(G)
    # for v in G.vertices:
    #     v.colornum = v.label
    # with open('mygraph.dot', 'w') as f:
    #     write_dot(G, f)

