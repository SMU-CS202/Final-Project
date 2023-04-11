import time
from brute_force import minimum_degree_spanning_tree

def test_brute_force(small_sparse_graphs,
                      small_dense_graphs,
                      medium_sparse_graphs,
                      medium_dense_graphs,
                      large_sparse_graphs,
                      large_dense_graphs):
    
    print("==========================================================================\n")
    total_time = 0
    for graph in range(len(small_sparse_graphs)):
        print(small_sparse_graphs[graph])
        t0 = time.time()
        print("TESTING SMALL SPARSE GRAPH", graph, ":")
        print(minimum_degree_spanning_tree(small_sparse_graphs[graph]))
        test_case_runtime = time.time() - t0
        total_time += test_case_runtime
        print("Time Taken: ", test_case_runtime, "\n")
    print("Total Time: ", total_time)
    print("Average Time: ", total_time / len(small_sparse_graphs))
    print("==========================================================================\n")

    total_time = 0
    for graph in range(len(small_dense_graphs)):
        t0 = time.time()
        print("TESTING SMALL DENSE GRAPH", graph, ":")
        print(minimum_degree_spanning_tree(small_dense_graphs[graph]))
        test_case_runtime = time.time() - t0
        total_time += test_case_runtime
        print("Time Taken: ", test_case_runtime, "\n")
    print("Total Time: ", total_time)
    print("Average Time: ", total_time / len(small_sparse_graphs))
    print("==========================================================================\n")

    total_time = 0
    for graph in range(len(medium_sparse_graphs)):
        t0 = time.time()
        print("TESTING MEDIUM SPARSE GRAPH", graph, ":")
        print(minimum_degree_spanning_tree(medium_sparse_graphs[graph]))
        test_case_runtime = time.time() - t0
        total_time += test_case_runtime
        print("Time Taken: ", test_case_runtime, "\n")
    print("Total Time: ", total_time)
    print("Average Time: ", total_time / len(small_sparse_graphs))
    print("==========================================================================\n")

    total_time = 0
    for graph in range(len(medium_dense_graphs)):
        t0 = time.time()
        print("TESTING MEDIUM DENSE GRAPH", graph, ":")
        print(minimum_degree_spanning_tree(medium_dense_graphs[graph]))
        test_case_runtime = time.time() - t0
        total_time += test_case_runtime
        print("Time Taken: ", test_case_runtime, "\n")
    print("Total Time: ", total_time)
    print("Average Time: ", total_time / len(small_sparse_graphs))
    print("==========================================================================\n")

    total_time = 0
    for graph in range(len(large_sparse_graphs)):
        t0 = time.time()
        print("TESTING LARGE SPARSE GRAPH", graph, ":")
        print(minimum_degree_spanning_tree(large_sparse_graphs[graph]))
        test_case_runtime = time.time() - t0
        total_time += test_case_runtime
        print("Time Taken: ", test_case_runtime, "\n")
    print("Total Time: ", total_time)
    print("Average Time: ", total_time / len(small_sparse_graphs))
    print("==========================================================================\n")

    total_time = 0
    for graph in range(len(large_dense_graphs)):
        t0 = time.time()
        print("TESTING LARGE DENSE GRAPH", graph, ":")
        print(minimum_degree_spanning_tree(large_dense_graphs[graph]))
        test_case_runtime = time.time() - t0
        total_time += test_case_runtime
        print("Time Taken: ", test_case_runtime, "\n")
    print("Total Time: ", total_time)
    print("Average Time: ", total_time / len(small_sparse_graphs))
    print("==========================================================================\n")
