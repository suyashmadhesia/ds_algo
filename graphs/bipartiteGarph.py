from collections import deque
from typing import List

"""
A graph is bipartite if you can split its nodes into two groups such that no two nodes within the same group are connected by an edge.

Step-by-Step BFS Intuition
    1. Start at an unvisited node, color it 0.
    2. For each neighbor, assign the opposite color (i.e., 1).
    3. If you ever reach a neighbor that is already colored the same as the current node, the graph is not bipartite.
Repeat for all disconnected components.

"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n  # -1 means uncolored

        for u in range(n):
            if colors[u] != -1:
                continue  # Already visited

            queue = deque([u])
            colors[u] = 0  # Start coloring

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False  # Conflict found

        return True

