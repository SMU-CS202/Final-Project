from collections import deque

def get_spanning_tree(graph):
    # Perform depth-first search to generate spanning tree
    visited = [False] * len(graph)  # initialize all vertices as not visited
    parent = [None] * len(graph)  # initialize parent array to store the spanning tree

    # DFS function to visit adjacent vertices recursively
    def dfs_visit(u):
        visited[u] = True  # mark current vertex as visited

        # loop through all adjacent vertices
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u  # set parent of adjacent vertex to current vertex
                dfs_visit(v)  # recursively visit adjacent vertex

    # call DFS on first vertex in graph
    dfs_visit(0)

    # build and return the spanning tree
    tree = [[] for _ in graph]
    for i, p in enumerate(parent):
        if p is not None:
            tree[i].append(p)
            tree[p].append(i)

    return tree