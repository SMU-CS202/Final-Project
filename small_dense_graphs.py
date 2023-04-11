import random
import copy

small_dense_graphs = []

complete_graph = {
        0: [1, 2, 3, 4],
        1: [0, 2, 3, 4],
        2: [0, 1, 3, 4],
        3: [0, 1, 2, 4],
        4: [0, 1, 2, 3]
}

for _ in range(10):
    num_of_edges_to_remove = random.randint(1, 2)
    new_dense_graph = copy.deepcopy(complete_graph)
    
    for i in range(num_of_edges_to_remove):
        while True:
            from_node = random.randint(0, 4)
            to_node = random.randint(0, 4)

            while True:
                if to_node == from_node or to_node not in new_dense_graph[from_node]:
                    from_node = random.randint(0, 4)
                    to_node = random.randint(0, 4)
                else:
                    break

            new_dense_graph[from_node].remove(to_node)
            new_dense_graph[to_node].remove(from_node)

            if new_dense_graph not in small_dense_graphs:
                break

            new_dense_graph = copy.deepcopy(complete_graph)

    small_dense_graphs.append(new_dense_graph)
