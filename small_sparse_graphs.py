import random
import copy

small_sparse_graphs = []

complete_graph = {
    0: [1, 2, 3, 4],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [0, 1, 2, 4],
    4: [0, 1, 2, 3]
}

for _ in range(10):
    num_of_edges_to_remove = 5
    new_sparse_graph = copy.deepcopy(complete_graph)

    for i in range(num_of_edges_to_remove):
        while True:
            from_node = random.randint(0, 5)
            to_node = random.randint(0, 5)

            while True:
                if to_node == from_node or not (from_node in new_sparse_graph and to_node in new_sparse_graph[from_node]):
                    from_node = random.randint(0, 5)
                    to_node = random.randint(0, 5)
                else:
                    break

            new_sparse_graph[from_node].remove(to_node)
            new_sparse_graph[to_node].remove(from_node)

            if new_sparse_graph not in small_sparse_graphs:
                break

            new_sparse_graph = copy.deepcopy(complete_graph)

    small_sparse_graphs.append(new_sparse_graph)
