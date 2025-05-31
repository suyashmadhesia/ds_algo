from heapq import heappush, heappop
from typing import List, Tuple

def prim_mst(n: int, adj: List[List[Tuple[int, int]]]) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Prim's Algorithm to find Minimum Spanning Tree (MST) of a graph.
    
    Parameters:
        n   : Number of nodes (0-indexed)
        adj : Adjacency list where adj[u] = [(v, weight), ...]
    
    Returns:
        total_cost : Total cost of MST
        mst_edges  : List of edges in MST as (u, v) tuples
    """

    visited = [False] * n
    min_heap = [(0, 0, -1)]  # (weight, current_node, parent_node)
    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, u, parent = heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += weight
        if parent != -1:
            mst_edges.append((parent, u))

        for v, w in adj[u]:
            if not visited[v]:
                heappush(min_heap, (w, v, u))

    return total_cost, mst_edges
