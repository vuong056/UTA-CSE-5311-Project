import networkx as nx
import heapq
import random
import time

from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns

def create_random_weighted_graph(vertex_count, edge_count):
    G = nx.gnm_random_graph(vertex_count, edge_count)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = int(100 * random.random()) + 1
    return G

#Adapted from <NetworkX Developers (2021). NetworkX: Minimum Spanning Tree: Kruskal's algorithm. 
#               Retrieved from https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.kruskal_mst.html>
def apply_kruskal_algorithm(G):
    edges = list(G.edges(data=True))
    edges.sort(key=lambda edge: edge[2]['weight'])

    parent = {node: node for node in G.nodes()}
    rank = defaultdict(int)

    def find_set(v):
        if parent[v] != v:
            parent[v] = find_set(parent[v])
        return parent[v]

    def union_sets(u, v):
        root_u = find_set(u)
        root_v = find_set(v)

        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_u] = root_v

                if rank[root_u] == rank[root_v]:
                    rank[root_v] += 1

    mst = []
    for u, v, weight in edges:
        if find_set(u) != find_set(v):
            union_sets(u, v)
            mst.append((u, v, weight))

            if len(mst) == G.number_of_nodes() - 1:
                break

    return mst
# Adapted from <NetworkX Developers (2021). NetworkX: Minimum Spanning Tree: Prim's algorithm. 
#               Retrieved from https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.minimum_spanning_edges.html>
def apply_prim_algorithm(G):
    mst = []
    visited = {list(G.nodes())[0]}
    edges = [
        (weight['weight'], u, v)
        for u, v, weight in G.edges(data=True)
        if u in visited or v in visited
    ]
    heapq.heapify(edges)

    while edges:
        weight, u, v = heapq.heappop(edges)

        if u not in visited:
            visited.add(u)
            mst.append((u, v, {'weight': weight}))

        if v not in visited:
            visited.add(v)
            mst.append((u, v, {'weight': weight}))

        for u_next, v_next, weight_next in G.edges(u, data=True):
            if v_next not in visited:
                heapq.heappush(edges, (weight_next['weight'], u_next, v_next))

        for u_next, v_next, weight_next in G.edges(v, data=True):
            if v_next not in visited:
                heapq.heappush(edges, (weight_next['weight'], u_next, v_next))

        if len(visited) == G.number_of_nodes():
            break

    return mst

def visualize_graph(G, kruskal_mst, prim_mst, graph_title):
    pos = nx.spring_layout(G)
    edge_labels = {(u, v): w['weight'] for u, v, w in G.edges(data=True)}

    # Original graph
    plt.figure(figsize=(10, 10))
    plt.title(f"{graph_title} - Original Graph")
    nx.draw(G, pos, with_labels=True, node_size=50, node_color="skyblue")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    sns.despine(left=True, bottom=True, top=False, right=False)
    plt.show()

    # MST found by Kruskal's algorithm
    plt.figure(figsize=(10, 10))
    plt.title(f"{graph_title} - MST (Kruskal's Algorithm)")
    nx.draw(G, pos, with_labels=True, node_size=50, node_color="skyblue", edgelist=[])
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v, _ in mst_kruskal], edge_color="r")
    sns.despine(left=True, bottom=True, top=False, right=False)
    plt.show()

    # MST found by Prim's algorithm
    plt.figure(figsize=(10, 10))
    plt.title(f"{graph_title} - MST (Prim's Algorithm)")
    nx.draw(G, pos, with_labels=True, node_size=50, node_color="skyblue", edgelist=[])
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v, _ in mst_prim], edge_color="r")
    sns.despine(left=True, bottom=True, top=False, right=False)
    plt.show()

def get_manual_graph_input():
    vertex_count = int(input("Enter the number of vertices: "))
    edge_count = int(input("Enter the number of edges: "))

    G = nx.Graph()

    for i in range(vertex_count):
        G.add_node(i)

    for i in range(edge_count):
        print(f"Enter the details for edge {i + 1}:")
        u = int(input("Enter the source vertex: "))
        v = int(input("Enter the target vertex: "))
        w = int(input("Enter the weight: "))
        G.add_edge(u, v, weight=w)

    return G

def measure_execution_times(vertex_counts, edge_counts):
    kruskal_times = []
    prim_times = []

    for v_count, e_count in zip(vertex_counts, edge_counts):
        graph = create_random_weighted_graph(v_count, e_count)

        # Measure Kruskal's algorithm execution time
        start_time = time.time()
        apply_kruskal_algorithm(graph)
        end_time = time.time()
        kruskal_times.append(end_time - start_time)

        # Measure Prim's algorithm execution time
        start_time = time.time()
        apply_prim_algorithm(graph)
        end_time = time.time()
        prim_times.append(end_time - start_time)

    return kruskal_times, prim_times

def charlie():
    vertex_counts = [10, 20, 30, 40, 50]
    edge_counts = [15, 30, 45, 60, 75]
    kruskal_times, prim_times = measure_execution_times(vertex_counts, edge_counts)
    plt.figure(figsize=(10, 6))
    plt.plot(vertex_counts, kruskal_times, marker='o', label="Kruskal's Algorithm")
    plt.plot(vertex_counts, prim_times, marker='s', label="Prim's Algorithm")
    plt.xlabel('Number of Vertices')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs. Input Size')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print("Enter 1 to generate a random weighted graph or 2 to input a graph manually:")
    user_choice = int(input())

    if user_choice == 1:
        vertex_count = int(input("Enter the number of vertices: "))
        edge_count = int(input("Enter the number of edges: "))
        graph = create_random_weighted_graph(vertex_count, edge_count)
    elif user_choice == 2:
        graph = get_manual_graph_input()
    elif user_choice == 3:
        charlie()
    else:
        print("Invalid choice. Exiting.")
        exit()

    # Apply Kruskal's algorithm and measure the execution time
    start_time = time.time()
    kruskal_mst = apply_kruskal_algorithm(graph)
    end_time = time.time()
    print(f"Kruskal's Algorithm Execution Time: {end_time - start_time:.4f} seconds")

    # Apply Prim's algorithm and measure the execution time
    start_time = time.time()
    prim_mst = apply_prim_algorithm(graph)
    end_time = time.time()
    print(f"Prim's Algorithm Execution Time: {end_time - start_time:.4f} seconds")

    # Visualize the graph
    visualize_graph(graph, kruskal_mst, prim_mst, "Random Weighted Graph")

    

    
