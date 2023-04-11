from itertools import chain, combinations

# *********************************************************************************
# *********************      MAIN FUNCTIONS       *********************************
# *********************************************************************************
def minimum_degree_spanning_tree(graph):
    vertices = graph.keys() # get all vertices in the graph
    all_valid_subgraphs = generate_subgraphs(graph) # get all valid subgraphs in the graph
    spanning_trees = get_all_spanning_trees(all_valid_subgraphs, graph) # get all subgraphs which are spanning trees
    if (len(spanning_trees) == 0):
        print("THERE ARE NO VALID SPANNING TREES.")
        return None
    mdst = get_smallest_degree(spanning_trees, len(vertices)) # get the MDST among all the spanning trees
    print("MST Degree: ", get_degree(mdst, len(vertices))) 
    return mdst

# Get all valid subgraphs of the graph
def generate_subgraphs(adj_list):
    powerV = powerset(adj_list.keys()) # generate all possible vertice permutations
    powerE = powerset(get_edges(adj_list)) # generate all possible edge permutations
    subgraphs = [] # keep a list of all valid subgraphs
    for V in powerV: # for every possible combination of vertices
        for E in powerE: # for every possible combination of edges
            accept = True # by default accept the combination
            for edge in E:
                # But if the edge vertices aren't present in the vertice set, it's not valid
                if(checkIfEdgeVerticesInSet(edge, V) == False): 
                    accept = False
            if (accept):
                subgraphs.append([V, E]) # dd valid subgraphs to the list of valid results
    return subgraphs

# Get all valid spanning trees, from the valid subgraphs
def get_all_spanning_trees(subgraphs, adj_list):
    spanning_trees = [] # store all valid spanning trees
    for subgraph in subgraphs:
        if (check_if_spanning(subgraph, adj_list)): # store it if it's a valid spanning tree
            spanning_trees.append(subgraph)
    return spanning_trees

# Out of all the spanning trees, get the one with the smallest degree
def get_smallest_degree(subgraphs, num_nodes):
    min_degree = float('inf')
    mdst = ""
    for subgraph in subgraphs:
        if (get_degree(subgraph, num_nodes) < min_degree and get_degree(subgraph, num_nodes) > 0):
            mdst = subgraph
            min_degree = get_degree(subgraph, num_nodes)
    return mdst

# *********************************************************************************
# *********************      HELPER FUNCTIONS       *******************************
# *********************************************************************************
def powerset(iterable): # get all possible combinations of elements in a set
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def get_degree(graph, num_nodes): # get the degree of the graph, only for an adjacency list
    adj_list = convert_edgelist_to_adj(graph[1], num_nodes)
    deg = -float('inf')
    for v in adj_list:
        deg = max(deg, len(adj_list[v]))
    return deg

def get_edges(adj_list): # get all edges of the graph, only for an adjacency list
    edges = []
    for key in adj_list.keys():
        for v in adj_list.get(key):
            if(v > key):
                edges.append([key, v])
    return edges

def checkIfVertexInSet(vertex, vertice_set): # check if a vertex can be found in a set of vertices
    found = False
    for v in vertice_set:
        if (vertex == v):
            found = True
    return found

def checkIfEdgeVerticesInSet(edge, Vset): # check if both vertices of an edge are present in a set of vertices
    u_found = checkIfVertexInSet(edge[0], Vset)
    v_found = checkIfVertexInSet(edge[1], Vset)
    if (v_found and u_found):
        return True
    return False

# Check if a vertex is contained within an edge
def check_if_vertex_in_edge(vertex, edge):
    if (vertex == edge[0] or vertex == edge[1]):
        return True
    return False

def convert_edgelist_to_adj(edges, num_nodes): # convert an edgelist to adjacency list for manipulation
    adj_matrix = [ [0] * num_nodes for i in range(num_nodes)] # first create an adjacency matrix
    for edge in edges:
        i = edge[0]
        j = edge[1]
        adj_matrix[i][j] = 1
        adj_matrix[j][i] = 1
    
    # Now build the adjacency list from the adjacency matrix
    adj_list = {}

    # First add keys, representing each node in the graph
    for i in range(num_nodes):
        adj_list[i] = []
    
    # Add neighbours for each  in the graph
    for i in range(num_nodes):
        for j in range(num_nodes):
            if (adj_matrix[i][j] == 1):
                adj_list[i].append(j)
    return adj_list

# For performing a DFS
def DFS(source, adj_list, visited_arr):
        # The source vertex has already been visited, mark it as visited
        visited_arr[source] = True

        # Visit the the neighbors of the source vertex
        for i in range(len(adj_list[source])):
            neighbour = adj_list[source][i]
            if(visited_arr[neighbour] == False):
                # Make recursive call from neighbor
                DFS(neighbour, adj_list, visited_arr)

# Perform a DFS on the graph. If all vertices have been visited, the graph is connected.
def check_if_connected(adj_list):
        # Store the number of vertices in the adjacency list
        num_vertices = len(adj_list.keys())
        
        # Create an array to store vertices which have been visited. Initialise to False by default
        visited = [False] * num_vertices

        # Start the DFS from the first vertex
        DFS(0, adj_list, visited)

        # The graph is connected if all nodes can be visited via a DFS
        count = 0
        for i in range(len(visited)):
            if(visited[i]):
                count += 1
        if(num_vertices == count):
            return True
        else:
            return False

# Check if a graph is spanning
def check_if_spanning(subgraph, adj_list):
    # A subgraph is spanning if it contains all vertices of the original graph and is connected
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