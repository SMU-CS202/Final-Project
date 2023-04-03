import random
import math
from random import sample
from spanning_tree import get_spanning_tree

# Local search algorithm for minimum degree spanning tree
def minimum_degree_spanning_tree(graph):
    # Initialize MST with minimum degree spanning tree
    num_vertex = len(graph)

    mst = get_spanning_tree(graph)
    
    mst_degree = get_degree(mst)
    print("MST DEGREE BEFORE:", mst_degree)

    if mst_degree == 2:
        print("MST DEGREE AFTER:", 2)
        return mst
    
    # Perform local search
    while True:
        # Find vertices u, v, and w for the local move
        candidates = [(u, v, w) for u in range(len(mst)) for v in range(num_vertex) for w in graph[v] if
                      get_vertex_degee(mst, u) >= get_degree(mst) - math.log2(num_vertex)
                      and is_on_path(mst, v, w, u, [])
                      and get_vertex_degee(mst, v) <= get_vertex_degee(mst,u) - 2
                      and get_vertex_degee(mst, w) <= get_vertex_degee(mst, u) - 2
                      and u != v
                      and u != w
                      and v != w]

        if not candidates:
            break  # no more moves possible

        u, v, w = sample(candidates, 1)[0]  # randomly choose one candidate

        # Update the tree T with the local move
        u_ = choose_u_neigh(mst, v, w, u)

        mst[u].remove(u_)
        mst[u_].remove(u)
        mst[v].append(w)
        mst[w].append(v)


    mst_degree = get_degree(mst)
    print("MST DEGREE AFTER:", mst_degree)
    
    return mst

def get_vertex_degee(graph, vertex):
    return len(graph[vertex])

def get_degree(graph):
    deg = -float('inf')

    for v in graph:
        deg = max(deg, len(v))

    return deg

def dfs(graph, start, visited, curr_path, w, u):
    visited.add(start)
    curr_path.add(start)

    print("curr: ", curr_path)

    for neighbor in graph[start]:
        if neighbor not in visited:
            if neighbor == w and u in curr_path:
                return True
            else:
                dfs(graph, neighbor, visited, curr_path, w, u)

    curr_path.remove(start)

def explore_all_paths(adj_list, v, u, visited, path, paths):
    visited[v] = True
    path.append(v)

    if v == u:
        paths.append(path.copy())
    else:
        for neighbor in adj_list[v]:
            if not visited[neighbor]:
                explore_all_paths(adj_list, neighbor, u, visited, path, paths)

    visited[v] = False
    path.pop()

def is_on_path(graph, v, w, u, paths):
    visited = [False] * len(graph)
    path = []
    explore_all_paths(graph, v, w, visited, path, paths)

    for path in paths:
        if u in path:
            return True

    return False

def choose_u_neigh(mst, v, w, u):
    u_neigh = set()

    paths = []
    is_on_path(mst, v, w, u, paths)

    for path in paths:
        for i in range(len(path)):
            if path[i] == u:
                if i - 1 >= 0:
                    u_neigh.add(path[i - 1])
                if i + 1 < len(path):
                    u_neigh.add(path[i + 1])
            continue

    u_ = random.choice(list(u_neigh)) # randomly choose one neighbour of u

    return u_
