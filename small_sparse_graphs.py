small_sparse_graphs = [
    [
        [1, 2],     # vertex 0 is connected to vertices 1 and 2
        [0, 3, 4],  # vertex 1 is connected to vertices 0, 3, and 4
        [0, 4],     # vertex 2 is connected to vertices 0 and 4
        [1, 4, 5],  # vertex 3 is connected to vertices 1, 4, and 5
        [1, 2, 3],  # vertex 4 is connected to vertices 1, 2, and 3
        [3]         # vertex 5 is connected to vertex 3
    ],
    [
        [1, 2, 3],  # neighbors of vertex 0
        [0, 4],     # neighbors of vertex 1
        [0, 4, 5],  # neighbors of vertex 2
        [0],        # neighbors of vertex 3
        [1, 2],     # neighbors of vertex 4
        [2]         # neighbors of vertex 5
    ],
    [
        [1, 2, 3],
        [0, 2, 4],
        [0, 1, 5],
        [0, 5],
        [1, 5, 6],
        [2, 3, 4, 7],
        [4],
        [5]
    ]
]