# UTA-CSE-5311-Project
Title: Minimum Spanning Tree Visualizer using Kruskal's and Prim's Algorithms

Introduction
This project aims to implement and visualize the Minimum Spanning Tree (MST) algorithms - Kruskal's and Prim's algorithms - on randomly generated or user-inputted weighted graphs. The visualizations will help users better understand the algorithms and their applications. The project also measures the execution times for both algorithms.

Data Structures and Algorithms
2.1 Graph Representation
The project uses NetworkX, a Python library for working with graphs. The graph is stored as a weighted undirected graph.

2.2 Kruskal's Algorithm
Kruskal's algorithm sorts the edges by weight and iteratively adds the edge with the lowest weight to the MST, as long as it doesn't form a cycle. It uses a disjoint-set data structure to keep track of the connected components of the MST.

2.3 Prim's Algorithm
Prim's algorithm starts with an arbitrary node and adds the edge with the smallest weight that connects a visited node with an unvisited node. It uses a priority queue (heap) to maintain the edges with the smallest weight.

Components of the Algorithm
3.1 generate_random_weighted_graph
This function generates a random weighted graph with a specified number of nodes and edges.

3.2 kruskal_algorithm
This function implements Kruskal's algorithm on a given graph and returns the MST as a list of edges.

3.3 prim_algorithm
This function implements Prim's algorithm on a given graph and returns the MST as a list of edges.

3.4 draw_graph
This function uses Matplotlib and Seaborn to visualize the original graph, the MST found by Kruskal's algorithm, and the MST found by Prim's algorithm.

3.5 input_graph
This function allows users to input a graph manually by specifying the number of vertices, edges, and their weights.

User Interface
The project does not use a GUI. It uses a command-line interface to interact with users, allowing them to choose between generating a random weighted graph or inputting a graph manually. Users can also input the number of vertices and edges for the graph.

Experimental Results
The project measures the execution time for both Kruskal's and Prim's algorithms. The execution time can be plotted against the input size (number of nodes and edges) to visualize the performance of the algorithms. In general, Kruskal's algorithm has a time complexity of O(E * log(E)), while Prim's algorithm has a time complexity of O(E * log(V)).

Conclusion
The Minimum Spanning Tree Visualizer effectively implements and visualizes Kruskal's and Prim's algorithms on weighted graphs. The project can help users understand the working of these algorithms and their applications in solving real-world problems. Additionally, the execution time measurements provide insights into the performance of the algorithms, allowing users to make informed decisions when choosing an algorithm for a specific task.
