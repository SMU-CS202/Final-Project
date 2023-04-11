from test_local_search import test_local_search
from test_brute_force import test_brute_force
from small_sparse_graphs import small_sparse_graphs
from small_dense_graphs import small_dense_graphs
from medium_sparse_graphs import medium_sparse_graphs
from medium_dense_graphs import medium_dense_graphs
from large_sparse_graphs import large_sparse_graphs
from large_dense_graphs import large_dense_graphs

print("===================== TESTING LOCAL SEARCH =====================")

test_local_search(small_sparse_graphs,
                  small_dense_graphs,
                  medium_sparse_graphs,
                  medium_dense_graphs,
                  large_sparse_graphs,
                  large_dense_graphs)

print("===================== TESTING BRUTE FORCE =====================")

test_brute_force(small_sparse_graphs,
                  small_dense_graphs,
                  medium_sparse_graphs,
                  medium_dense_graphs,
                  large_sparse_graphs,
                  large_dense_graphs)
