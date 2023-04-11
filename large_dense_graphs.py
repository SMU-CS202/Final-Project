import random
import copy

complete_graph = [[i for i in range(15)] for j in range(15)]

for i in range(15):
    complete_graph[i].remove(i)

large_dense_graphs = []

for _ in range(10):
    num_of_edges_to_remove = random.randint(25, 35)
    new_dense_graph = copy.deepcopy(complete_graph)
    
    for i in range(num_of_edges_to_remove):
        while True:
            from_node = random.randint(0, 14)
            to_node = random.randint(0, 14)

            while True:
                if to_node == from_node or to_node not in new_dense_graph[from_node]:
                    from_node = random.randint(0, 14)
                    to_node = random.randint(0, 14)
                else:
                    break

            new_dense_graph[from_node].remove(to_node)
            new_dense_graph[to_node].remove(from_node)

            if new_dense_graph not in large_dense_graphs:
                break

            new_dense_graph = copy.deepcopy(complete_graph)

    large_dense_graphs.append(new_dense_graph)
