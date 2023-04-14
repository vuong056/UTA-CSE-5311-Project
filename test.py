import networkx as nx
from operator import itemgetter
from collections import defaultdict
import heapq
import time
import random

def generate_random_weighted_graph(n, m):
    G = nx.gnm_random_graph(n, m)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = int(100 * random.random()) + 1
    return G


def kruskal_algorithm(G):
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

def prim_algorithm(G):
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


if __name__ == "__main__":
    num_vertices = 1000
    num_edges = 2000

    # Generate a random weighted graph
    graph = generate_random_weighted_graph(num_vertices, num_edges)

    # Apply Kruskal's algorithm and measure the execution time
    start_time = time.time()
    mst_kruskal = kruskal_algorithm(graph)
    end_time = time.time()
    print(f"Kruskal's Algorithm Execution Time: {end_time - start_time:.4f} seconds")

    # Apply Prim's algorithm and measure the execution time
    start_time = time.time()
    mst_prim = prim_algorithm(graph)
    end_time = time.time()
    print(f"Prim's Algorithm Execution Time: {end_time - start_time:.4f} seconds")

    print(graph)
