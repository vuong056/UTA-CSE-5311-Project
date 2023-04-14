# UTA-CSE-5311-Project

This project aims to compare Kruskal's and Prim's algorithms for finding minimum spanning trees (MST) in a graph. We generate random graphs using the networkx library, apply the two algorithms, and measure their execution times.

Import necessary libraries:
networkx for generating and working with graphs.
itemgetter for sorting edges by weight.
defaultdict for initializing node ranks.
heapq for creating and managing a priority queue.
time for measuring algorithm execution times.
random for generating random edge weights.

Define generate_random_weighted_graph(n, m) function:
Generate a random graph with n nodes and m edges using the networkx library.
Assign random weights between 1 and 100 to each edge.

Implement Kruskal's algorithm:
Sort edges by weight in ascending order.
Initialize node parents and ranks.
Define helper functions find_set and union_sets for disjoint-set data structure.
Iterate through the sorted edges, add them to the MST if they don't form a cycle, and union their sets.

Implement Prim's algorithm:
Initialize an empty MST, a set of visited nodes, and a list of candidate edges.
Create a min-heap from the candidate edges.
While there are candidate edges:
Pop the edge with the smallest weight from the heap.
If either endpoint is not visited, add the edge to the MST and update the visited set.
Add new candidate edges connected to the visited endpoints to the heap.

Main script:
Generate a random weighted graph with 1000 nodes and 2000 edges.
Apply Kruskal's algorithm and measure the execution time.
Apply Prim's algorithm and measure the execution time.
Print the execution times for both algorithms.

With this project, you can compare the execution times of Kruskal's and Prim's algorithms on a randomly generated graph. This helps you understand their performance characteristics and evaluate their efficiency for different graph sizes and densities.
