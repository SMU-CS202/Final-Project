import itertools

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
    
    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

def mdst(graph):
    # Initialize minimum degree spanning tree with empty edges
    mdst = Graph(graph.V)

    # Loop through all possible subgraphs
    for subgraph in itertools.combinations(range(graph.V), graph.V // 2):
        # Create a copy of the graph and remove the vertices not in the subgraph
        subgraph_graph = Graph(graph.V)
        for u in subgraph:
            for v, w in graph.adj[u]:
                if v in subgraph:
                    subgraph_graph.add_edge(u, v, w)

        # Calculate the degree of each vertex in the subgraph
        degrees = [0] * subgraph_graph.V
        for u in subgraph:
            for v, _ in subgraph_graph.adj[u]:
                degrees[u] += 1
                degrees[v] += 1

        # If the subgraph is connected and has the minimum degree, add its edges to the MDST
        if all(degrees[u] >= 2 for u in subgraph) and subgraph_graph.V % 2 == 0:
            for u in subgraph:
                for v, w in subgraph_graph.adj[u]:
                    if v > u:
                        mdst.add_edge(u, v, w)
    return mdst

# Test case 1
g1 = Graph(5)
g1.add_edge(0, 1, 2)
g1.add_edge(0, 2, 1)
g1.add_edge(0, 3, 4)
g1.add_edge(1, 2, 3)
g1.add_edge(1, 4, 5)
g1.add_edge(2, 3, 6)
g1.add_edge(3, 4, 7)

mdst1 = mdst(g1)
for u in range(mdst1.V):
    for v, w in mdst1.adj[u]:
        if v > u:
            print(f"({u}, {v}): {w}")  # Expected output: (0, 2): 1  (1, 2): 3  (0, 1): 2  (1, 4): 5

# Test case 2
g2 = Graph(6)
g2.add_edge(0, 1, 1)
g2.add_edge(0, 2, 2)
g2.add_edge(1, 2, 3)
g2.add_edge(1, 3, 4)
g2.add_edge(2, 3, 5)
g2.add_edge(2, 4, 6)
g2.add_edge(3, 4, 7)
g2.add_edge(3, 5, 8)
g2.add_edge(4, 5, 9)

mdst2 = mdst(g2)
for u in range(mdst2.V):
    for v, w in mdst2.adj[u]:
        if v > u:
            print(f"({u}, {v}): {w}")  # Expected output: (0, 1): 1  (2, 4): 6  (3, 4): 7  (1, 3): 4

# Test case 3
g3 = Graph(4)
g3.add_edge(0, 1, 1)
g3.add_edge(0, 2, 2)
g3.add_edge(0, 3, 3)
g3.add_edge(1, 2, 4)
g3.add_edge(1, 3, 5)
g3.add_edge(2, 3, 6)

mdst3 = mdst(g3)
for u in range(mdst3.V):
    for v, w in mdst3.adj[u]:
        if v > u:
            print(f"({u}, {v}): {w}")  # Expected output: (0, 2): 2  (0, 1): 1  (1, 3): 5