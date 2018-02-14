# from graphs.mygraph import del_edge
from graphs.graph_io import load_graph, write_dot # graphIO import graphs.py, so we do not need to import it here.
import os
import math

# Use these options to change the tests:

TEST_BELLMAN_FORD_DIRECTED = True
TEST_BELLMAN_FORD_UNDIRECTED = True
TEST_DIJKSTRA_DIRECTED = True
TEST_DIJKSTRA_UNDIRECTED = True

WRITE_DOT_FILES = False

# Use this to select the graphs to test your algorithms on:
# TestInstances = ["examples/weightedexample.gr"]
# TestInstances=["examples/randomplanar.gr"]
# TestInstances = ["examples/randomplanar10.gr"]
# TestInstances=["examples/bd.gr","examples/bbf.gr"]; WriteDOTFiles=False
# TestInstances=["examples/bbf2000.gr"]; WriteDOTFiles=False
# TestInstances=["examples/bbf200.gr"]
# TestInstances=["examples/negativeweightexample.gr"]
# TestInstances=["examples/negativeweightcycleexample.gr"]
TestInstances=["examples/WDE100.gr","examples/WDE200.gr","examples/WDE400.gr","examples/WDE800.gr","examples/WDE2000.gr"]; WriteDOTFiles=False
# TestInstances=["examples/weightedex500.gr"];	WriteDOTFiles=False


USE_UNSAFE_GRAPH = False


def bellman_ford_undirected(graph, start):
    """
    Arguments: <graph> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <graph>.
    Action: Uses the Bellman-Ford algorithm to compute all vertex distances
        from <start> in <graph>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <graph> is viewed as an undirected graph.
    """
    # Initialize the vertex attributes:
    for v in graph.vertices:
        v.dist = math.inf
        v.in_edge = None

    start.dist = 0

    # Insert your code here.
    # check for negative cycles
    for e in graph.edges:
        if e.weight < 0:
            raise ValueError('There is a negative cycle in this graph, because there is an edge with a negative number')

    did_not_update = False
    for i in graph.vertices + graph.vertices:
        if did_not_update:
            break
        else:
            did_not_update = True
            for e in graph.edges:
                if e.tail.dist + e.weight < e.head.dist:
                    e.head.dist = e.tail.dist + e.weight
                    e.head.in_edge = e.tail
                    did_not_update = False
                elif e.tail.dist > e.weight + e.head.dist:
                    e.tail.dist = e.head.dist + e.weight
                    e.tail.in_edge = e.head
                    did_not_update = False


def bellman_ford_directed(graph, start):
    """
    Arguments: <graph> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <graph>.
    Action: Uses the Bellman-Ford algorithm to compute all vertex distances
        from <start> in <graph>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <graph> is viewed as a directed graph.
    """
    # Initialize the vertex attributes:
    for v in graph.vertices:
        v.dist = math.inf
        v.in_edge = None

    start.dist = 0

    # Insert your code here.
    did_not_update = False
    for i in graph.vertices:
        if did_not_update:
            break
        else:
            did_not_update = True
            for e in graph.edges:
                if e.tail.dist + e.weight < e.head.dist:
                    e.head.dist = e.tail.dist + e.weight
                    e.head.in_edge = e.tail
                    did_not_update = False

    # check for negative cycles
    for e in graph.edges:
        if e.tail.dist + e.weight < e.head.dist:
            raise ValueError('There is a negative cycle in this graph')


def dijkstra_undirected(graph, start):
    """
    Arguments: <graph> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <graph>.
    Action: Uses Dijkstra's algorithm to compute all vertex distances
        from <start> in <graph>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <graph> is viewed as an undirected graph.
    """
    # Initialize the vertex attributes:
    for v in graph.vertices:
        v.dist = math.inf
        v.in_edge = None

    start.dist = 0

    # Insert your code here.
    for e in graph.edges:
        if e.weight < 0:
            raise ValueError('You cannot apply Dijkstra on a graph with negative edges')

    visited = []
    tobevisited = graph.vertices
    while len(tobevisited) is not 0:
        vmin = tobevisited[0]
        for v in tobevisited:
            if v.dist < vmin.dist:
                vmin = v
        visited = visited + [vmin]
        tobevisited.remove(vmin)
        for e in vmin.incidence:
            if e.tail.dist + e.weight < e.head.dist:
                e.head.dist = e.tail.dist + e.weight
                e.head.in_edge = e.tail
            elif e.tail.dist > e.weight + e.head.dist:
                e.tail.dist = e.head.dist + e.weight
                e.tail.in_edge = e.head

def dijkstra_directed(graph, start):
    """
    Arguments: <graph> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <graph>.
    Action: Uses Dijkstra's algorithm to compute all vertex distances
        from <start> in <graph>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <graph> is viewed as a directed graph.
    """
    # Initialize the vertex attributes:
    for v in graph.vertices:
        v.dist = math.inf
        v.in_edge = None

    start.dist = 0

    # Insert your code here.
    for e in graph.edges:
        if e.weight < 0:
            raise ValueError('You cannot apply Dijkstra on a graph with negative edges')

    visited = []
    tobevisited = graph.vertices
    while len(tobevisited) is not 0:
        vmin = tobevisited[0]
        for v in tobevisited:
            if v.dist < vmin.dist:
                vmin = v
        visited = visited + [vmin]
        tobevisited.remove(vmin)
        for e in vmin.incidence:
            if e.tail.dist + e.weight < e.head.dist:
                e.head.dist = e.tail.dist + e.weight
                e.head.in_edge = e.tail





##############################################################################
#
# Below is test code that does not need to be changed.
#
##############################################################################

def print_max_dist(graph):
    unreachable = False
    numreachable = 0
    sorted_vertices = sorted(graph.vertices, key=lambda v: v.label)
    remote = sorted_vertices[0]
    for v in graph.vertices:
        if v.dist == math.inf:
            unreachable = True
            # print("Vertex", v,"is unreachable")
        else:
            numreachable += 1
            if v.dist > remote.dist:
                remote = v
    print("Number of reachable vertices:", numreachable, "out of", len(graph))
    print("Largest distance:", remote.dist, "For vertex", remote)


def prepare_drawing(graph):
    for e in graph.edges:
        e.colornum = 0
    for v in graph.vertices:
        if hasattr(v, "in_edge") and v.in_edge is not None:
            v.in_edge.colornum = 1
    for v in graph:
        v.label = str(v.dist)


def do_testalg(testalg, G):
    if testalg[1]:
        print("\n\nTesting", testalg[0])
        startt = time()
        if testalg[0] == "Kruskal":
            ST = testalg[2](G)
            totalweight = 0
            for e in ST:
                totalweight += e.weight
        else:
            sorted_vertices = sorted(G.vertices, key=lambda v: v.label)
            testalg[2](G, sorted_vertices[0])
        endt = time()
        print("Elapsed time in seconds:", endt - startt)

        if testalg[0] != "Kruskal":
            print_max_dist(G)
            prepare_drawing(G)
        else:
            if len(ST) < len(G.vertices) - 1:
                print("Total weight of maximal spanning forest:", totalweight)
            else:
                print("Total weight of spanning tree:", totalweight)
            for e in G.edges:
                e.colornum = 0
            for e in ST:
                e.colornum = 1
            for v in G.vertices:
                v.label = v._label

        if WRITE_DOT_FILES:
            with open(os.path.join(os.getcwd(), testalg[3] + '.dot'), 'w') as f:
                write_dot(G, f, directed=testalg[4])


if __name__ == "__main__":
    from time import time

    for FileName in TestInstances:
        # Tuple arguments below:
        # First: printable string
        # Second: Boolean value
        # Third: Function
        # Fourth: Filename
        # Fifth: Whether output should be directed
        for testalg in [("Bellman-Ford, undirected", TEST_BELLMAN_FORD_UNDIRECTED, bellman_ford_undirected,
                         "BellmanFordUndirected", False),
                        ("Bellman-Ford, directed", TEST_BELLMAN_FORD_DIRECTED, bellman_ford_directed, "BellmanFordDirected",
                         True),
                        ("Dijkstra, undirected", TEST_DIJKSTRA_UNDIRECTED, dijkstra_undirected, "DijkstraUndirected",
                         False),
                        ("Dijkstra, directed", TEST_DIJKSTRA_DIRECTED, dijkstra_directed, "DijkstraDirected", True)]:
            if USE_UNSAFE_GRAPH:
                print("\n\nLoading graph", FileName, "(Fast graph)")
                with open(os.path.join(os.getcwd(), FileName)) as f:
                    G = load_graph(f, graph.Graph)
            else:
                print("\n\nLoading graph", FileName)
                with open(os.path.join(os.getcwd(), FileName)) as f:
                    G = load_graph(f)

            for i, vertex in enumerate(list(G.vertices)):
                vertex.colornum = i
            do_testalg(testalg, G)
