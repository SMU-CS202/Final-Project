from local_search import minimum_degree_spanning_tree
from small_sparse_graphs import small_sparse_graphs

for graph in range(len(small_sparse_graphs)):
    print("TESTING SMALL SPARSE GRAPH", graph, ":")
    print(minimum_degree_spanning_tree(small_sparse_graphs[graph]), "\n")
