from local_search import minimum_degree_spanning_tree
from small_sparse_graphs import small_sparse_graphs
from small_dense_graphs import small_dense_graphs

print("==========================================================================\n")

for graph in range(len(small_sparse_graphs)):
    print("TESTING SMALL SPARSE GRAPH", graph, ":")
    print(minimum_degree_spanning_tree(small_sparse_graphs[graph]), "\n")

print("==========================================================================\n")

for graph in range(len(small_dense_graphs)):
    print("TESTING SMALL DENSE GRAPH", graph, ":")
    print(minimum_degree_spanning_tree(small_dense_graphs[graph]), "\n")

print("==========================================================================\n")