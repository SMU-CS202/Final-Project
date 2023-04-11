from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def get_degree(graph):
    deg = -float('inf')
    for v in graph:
        deg = max(deg, len(v))
    return deg

def get_smallest_degree(subgraphs):
    min_degree = float('inf')
    mdst = ""
    for subgraph in subgraphs:
        if (get_degree(subgraph) < min_degree):
            mdst = subgraph
            min_degree = get_degree(subgraph)
    return mdst

def get_edges(adj_list):
    edges = []
    for key in adj_list.keys():
        for v in adj_list.get(key):
            if(v > key):
                edges.append([key, v])
    return edges

def checkIfVertexInSet(vertex, vertice_set):
    found = False
    for v in vertice_set:
        if (vertex == v):
            found = True
    return found

def checkIfEdgeVerticesInSet(edge, Vset):
    u_found = checkIfVertexInSet(edge[0], Vset)
    v_found = checkIfVertexInSet(edge[1], Vset)
    if (v_found and u_found):
        return True
    return False

def convert_edgelist_to_adj(edges, num_nodes):
    adj_matrix = [ [0] * num_nodes for i in range(num_nodes)]
    for edge in edges:
        i = edge[0]
        j = edge[1]
        adj_matrix[i][j] = 1
        adj_matrix[j][i] = 1
    adj_list = {}
    # Now build the adjacency list
    # First add keys
    for i in range(num_nodes):
        adj_list[i] = []
    
    # Add neighbours for each node
    for i in range(num_nodes):
        for j in range(num_nodes):
            if (adj_matrix[i][j] == 1):
                adj_list[i].append(j)
    return adj_list

def DFS(source, adj_list, visited_arr):
        # Mark the vertex visited
        visited_arr[source] = True

        # Visit the the neighbors
        for i in range(len(adj_list[source])):
            neighbour = adj_list[source][i]
            if(visited_arr[neighbour] == False):
                # Make recursive call from neighbor
                DFS(neighbour, adj_list, visited_arr)

def check_if_connected(adj_list):
        num_vertices = len(adj_list.keys())

        # Create array to store visited nodes
        visited = [False] * num_vertices

        # Begin the DFS from vertex 0
        DFS(0, adj_list, visited)

        # Check if all the vertices are visited, if yes then graph is connected
        count = 0
        for i in range(len(visited)):
            if(visited[i]):
                count += 1
        if(num_vertices == count):
            print("Given graph is connected")
            print(adj_list)
            return True
        else:
            print("Given graph is not connected")
            return False

def generate_subgraphs(adj_list):
    powerV = powerset(adj_list.keys()) # generate all possible vertice permutations
    powerE = powerset(get_edges(adj_list)) # generate all possible edge permutations
    subgraphs = []
    for V in powerV:
        for E in powerE:
            accept = True
            for edge in E:
                if(checkIfEdgeVerticesInSet(edge, V) == False):
                    accept = False
            if (accept):
                subgraphs.append([V, E])
    return subgraphs

def check_if_vertex_in_edge(vertex, edge):
    if (vertex == edge[0] or vertex == edge[1]):
        return True
    return False

def check_if_spanning(subgraph, adj_list):
    subgraph_edges = subgraph[1]
    vertices = adj_list.keys() # get all vertices in the graph
    record_vertex_present = [False] * len(vertices) # keep track of the presence of each vertex in the graph

    for edge in subgraph_edges:
        record_vertex_present[edge[0]] = True
        record_vertex_present[edge[1]] = True
    
    for i in range(len(record_vertex_present)):
        if (record_vertex_present[i] == False):
            return False
    subgraph_to_adj = convert_edgelist_to_adj(subgraph_edges, len(vertices))
    if (check_if_connected(subgraph_to_adj)):
        return True
    return False

def get_all_spanning_trees(subgraphs, adj_list):
    spanning_trees = []
    for subgraph in subgraphs:
        if (check_if_spanning(subgraph, adj_list)):
            spanning_trees.append(subgraph)
    return spanning_trees

def minimum_degree_spanning_tree(graph):
    vertices = graph.keys() # get all verticees
    all_valid_subgraphs = generate_subgraphs(graph)
    spanning_trees = get_all_spanning_trees(all_valid_subgraphs, graph)
    mdst = get_smallest_degree(spanning_trees)
    return mdst
