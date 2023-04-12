### Testing 

#### Local Search and Brute Force together
To test both the Local Search and Brute Force algorithms with the same inputs, run the following command in the root directory:

`python test.py` or `python3 test.py`

However, note that it is reccomended to manually interrupt this test (`cntrl + c` or `cmd + c`) or it will run for hours due to the astronomical time complexity of the Brute Force algorithm.

#### Local Search

##### Small, Medium and Large
To test just the Local Search algorithm for small, medium and large graphs, run the following command in the root directory: 

`python test_local_search.py` or `python3 test_local_search.py`


##### Extremely Large
To test just the Local Search algorithm for extremely large graphs, run the following command in the root directory: 

`python test_local_search_extremely_large.py` or `python3 test_local_search_extremely_large.py`

#### Brute Force

##### Small, Medium and Large
To test just the Brute Force algorithm for small, medium and large graphs, run the following command in the root directory: 

`python test_local_search.py` or `python3 test_brute_force.py`

However, note that similar to what was mentioned above, it is reccomended to manually interrupt this test (`cntrl + c` or `cmd + c`) as it will run for hours due to the astronomical time complexity of the algorithm.

##### Extremely Large
Since the medium test cases already take hours, there is no test cases for extremely large graphs.
