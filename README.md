# UTA-CSE-5311-Project
# Minimum Spanning Tree Visualizer using Kruskal's and Prim's Algorithms

## 1. Introduction
Using weighted graphs that are generated randomly or by the user, this project aims to implement and visualize the Minimum Spanning Tree (MST) algorithms developed by Kruskal and Prim. Users will gain a better understanding of the algorithms and their uses from the visualizations. Additionally, both algorithms' execution times are being measured for the project.

## 2. Data Structures and Algorithms
### 2.1 Graph Representation
The project uses NetworkX, a Python library for working with graphs. The graph is stored as a weighted undirected graph.

### 2.2 Kruskal's Algorithm
Kruskal's algorithm sorts the edges by weight and iteratively adds the edge with the lowest weight to the MST, as long as it doesn't form a cycle. It uses a disjoint-set data structure to keep track of the connected components of the MST.

### 2.3 Prim's Algorithm
Prim's algorithm starts with an arbitrary node and adds the edge with the smallest weight that connects a visited node with an unvisited node. It uses a priority queue (heap) to maintain the edges with the smallest weight.

## 3. Components of the Algorithm
### 3.1 create_random_weighted_graph
A random weighted graph with a predetermined number of nodes and edges is generated by this function.

### 3.2 apply_kruskal_algorithm
On a given graph, this function applies Kruskal's algorithm and outputs the MST as a list of edges.

### 3.3 apply_prim_algorithm
On a given graph, this function applies Prim's algorithm and outputs the MST as a list of edges.

### 3.4 visualize_graph
The original graph, the MST discovered by Kruskal's algorithm, and the MST discovered by Prim's algorithm are all visualized by this function using Matplotlib and Seaborn.

### 3.5 get_manual_graph_input
With the help of this function, users can manually enter a graph by indicating its vertex, edge, and weight counts. ST found by Kruskal's algorithm, and the MST found by Prim's algorithm.

## 4. User Interface
The project does not use a GUI. It uses a command-line interface to interact with users, allowing them to choose between generating a random weighted graph or inputting a graph manually. Users can also input the number of vertices and edges for the graph.

## 5. Experimental Results
The project measures the execution time for both Kruskal's and Prim's algorithms. The execution time can be plotted against the input size (number of nodes and edges) to visualize the performance of the algorithms. In general, Kruskal's algorithm has a time complexity of O(E * log(E)), while Prim's algorithm has a time complexity of O(E * log(V)).

![alt text](https://github.com/vuong056/UTA-CSE-5311-Project/blob/main/Figure_1.png)


## 6. Conclusion
On weighted graphs, the Kruskal and Prim algorithms are successfully implemented and visualized by the Minimum Spanning Tree Visualizer. The project can assist users in comprehending how these algorithms function and how they are used to address problems in the real world. Additionally, the execution time measurements give users information about the performance of the algorithms so they can choose the best algorithm for a given task.


## Citation
1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms (3rd ed.). MIT Press.
2. NetworkX Developers (2021). NetworkX: Minimum Spanning Tree: Prim's algorithm. Retrieved from https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.minimum_spanning_edges.html
3. NetworkX Developers (2021). NetworkX: Minimum Spanning Tree: Kruskal's algorithm. Retrieved from https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.kruskal_mst.html

