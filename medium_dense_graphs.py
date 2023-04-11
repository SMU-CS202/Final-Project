import random
import copy

medium_dense_graphs = []

complete_graph = {
        0: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        1: [0, 2, 3, 4, 5, 6, 7, 8, 9],
        2: [0, 1, 3, 4, 5, 6, 7, 8, 9],
        3: [0, 1, 2, 4, 5, 6, 7, 8, 9],
        4: [0, 1, 2, 3, 5, 6, 7, 8, 9],
        5: [0, 1, 2, 3, 4, 6, 7, 8, 9],
        6: [0, 1, 2, 3, 4, 5, 7, 8, 9],
        7: [0, 1, 2, 3, 4, 5, 6, 8, 9],
        8: [0, 1, 2, 3, 4, 5, 6, 7, 9],
        9: [0, 1, 2, 3, 4, 5, 6, 7, 8]
}

for _ in range(10):
    num_of_edges_to_remove = random.randint(15, 25)
    new_dense_graph = copy.deepcopy(complete_graph)

    for i in range(num_of_edges_to_remove):
        while True:
            from_node = random.randint(0, 9)
            to_node = random.randint(0, 9)

            while True:
                if to_node == from_node or to_node not in new_dense_graph[from_node]:
                    from_node = random.randint(0, 9)
                    to_node = random.randint(0, 9)
                else:
                    break

            new_dense_graph[from_node].remove(to_node)
            new_dense_graph[to_node].remove(from_node)

            if new_dense_graph not in medium_dense_graphs:
                break

            new_dense_graph = copy.deepcopy(complete_graph)
            
    medium_dense_graphs.append(new_dense_graph)
