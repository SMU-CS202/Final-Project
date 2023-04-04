import random

extremely_large_sparse_graph = [[i for i in range(100)] for j in range(100)]

for i in range(100):
    extremely_large_sparse_graph[i].remove(i)

num_of_edges_to_remove = random.randint(3450, 4450)

for i in range(num_of_edges_to_remove):
    from_node = random.randint(0, 99)
    to_node = random.randint(0, 99)

    while True:
        if to_node == from_node or to_node not in extremely_large_sparse_graph[from_node]:
            from_node = random.randint(0, 99)
            to_node = random.randint(0, 99)
        else:
            break

    extremely_large_sparse_graph[from_node].remove(to_node)
    extremely_large_sparse_graph[to_node].remove(from_node)
