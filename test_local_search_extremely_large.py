import time
from local_search import minimum_degree_spanning_tree
from extremely_large_dense_graph import extremely_large_dense_graph
from extremely_large_sparse_graph import extremely_large_sparse_graph

print("==========================================================================\n")

t0 = time.time()
print("TESTING EXTREMELY LARGE SPARSE GRAPH :")
print(minimum_degree_spanning_tree(extremely_large_sparse_graph))
print("Time Taken:", time.time() - t0, "\n")

print("==========================================================================\n")

t0 = time.time()
print("TESTING EXTREMELY LARGE DENSE GRAPH :")
print(minimum_degree_spanning_tree(extremely_large_dense_graph))
print("Time Taken:", time.time() - t0, "\n")
