import random
import copy

complete_graph = [[i for i in range(100)] for j in range(100)]

for i in range(100):
    complete_graph[i].remove(i)

large_sparse_graphs = [complete_graph]

for _ in range(10):
    num_of_edges_to_remove = random.randint(3450, 4450)
    new_sparse_graph = copy.deepcopy(complete_graph)

    for i in range(num_of_edges_to_remove):
        while True:
            from_node = random.randint(0, 99)
            to_node = random.randint(0, 99)

            while True:
                if to_node == from_node or to_node not in new_sparse_graph[from_node]:
                    from_node = random.randint(0, 99)
                    to_node = random.randint(0, 99)
                else:
                    break

            new_sparse_graph[from_node].remove(to_node)
            new_sparse_graph[to_node].remove(from_node)

            if new_sparse_graph not in large_sparse_graphs:
                break
                
            new_sparse_graph = copy.deepcopy(complete_graph)

    large_sparse_graphs.append(new_sparse_graph)
