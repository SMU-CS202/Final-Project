import time
from local_search import minimum_degree_spanning_tree
from small_sparse_graphs import small_sparse_graphs
from small_dense_graphs import small_dense_graphs
from medium_sparse_graphs import medium_sparse_graphs
from medium_dense_graphs import medium_dense_graphs
from large_sparse_graphs import large_sparse_graphs
from large_dense_graphs import large_dense_graphs

print("==========================================================================\n")

for graph in range(len(small_sparse_graphs)):
    t0 = time.time()
    print("TESTING SMALL SPARSE GRAPH", graph, ":")
    print(minimum_degree_spanning_tree(small_sparse_graphs[graph]))
    print("Time Taken:", time.time() - t0, "\n")

print("==========================================================================\n")

for graph in range(len(small_dense_graphs)):
    t0 = time.time()
    print("TESTING SMALL DENSE GRAPH", graph, ":")
    print(minimum_degree_spanning_tree(small_dense_graphs[graph]))
    print("Time Taken:", time.time() - t0, "\n")

print("==========================================================================\n")

for graph in range(len(medium_sparse_graphs)):
    t0 = time.time()
    print("TESTING MEDIUM SPARSE GRAPH", graph, ":")
    print(minimum_degree_spanning_tree(medium_sparse_graphs[graph]))
    print("Time Taken:", time.time() - t0, "\n")

print("==========================================================================\n")

for graph in range(len(medium_dense_graphs)):
    t0 = time.time()
    print("TESTING MEDIUM DENSE GRAPH", graph, ":")
    print(minimum_degree_spanning_tree(medium_dense_graphs[graph]))
    print("Time Taken:", time.time() - t0, "\n")

print("==========================================================================\n")

for graph in range(len(large_sparse_graphs)):
    t0 = time.time()
    print("TESTING LARGE SPARSE GRAPH", graph, ":")
    print(minimum_degree_spanning_tree(large_sparse_graphs[graph]))
    print("Time Taken:", time.time() - t0, "\n")

print("==========================================================================\n")

for graph in range(len(large_dense_graphs)):
    t0 = time.time()
    print("TESTING LARGE DENSE GRAPH", graph, ":")
    print(minimum_degree_spanning_tree(large_dense_graphs[graph]))
    print("Time Taken:", time.time() - t0, "\n")

print("==========================================================================\n")
