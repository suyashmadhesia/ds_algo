"""
Key Concepts
Graph: Set of nodes (vertices) connected by edges.
Weight: Cost or distance between two nodes.
Priority Queue / Min-Heap: Used to always expand the node with the shortest distance found so far.

📜 Algorithm Steps
Given:
Graph G = (V, E) where V is the set of vertices and E is the set of edges with weights.

A source node S.

1. Initialization
Set distance to all nodes as ∞, except the source node, which is 0.
Mark all nodes as unvisited.
Use a min-priority queue (min-heap) to store (distance, node) pairs.

2. Main Loop
While the queue is not empty:
Extract the node u with the smallest distance from the queue.
For each neighbor v of u:
Calculate new_distance = dist[u] + weight(u, v)
If new_distance < dist[v], update dist[v] and push (dist[v], v) into the queue.

3. Result
At the end, dist[] contains the shortest distances from source to all nodes.


✅ Conditions for Dijkstra
Graph must have non-negative weights

Efficient with a priority queue (like min-heap)

Questions on dijkstra

| #  | Title                                                | Difficulty | Link                                                                                    |
| -- | ---------------------------------------------------- | ---------- | --------------------------------------------------------------------------------------- |
| 1  | **743. Network Delay Time**                          | Medium     | [🔗 LeetCode](https://leetcode.com/problems/network-delay-time)                         |
| 2  | **1631. Path With Minimum Effort**                   | Medium     | [🔗 LeetCode](https://leetcode.com/problems/path-with-minimum-effort)                   |
| 3  | **1514. Path with Maximum Probability**              | Medium     | [🔗 LeetCode](https://leetcode.com/problems/path-with-maximum-probability)              |
| 4  | **787. Cheapest Flights Within K Stops**             | Medium     | [🔗 LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops)            |
| 5  | **882. Reachable Nodes In Subdivided Graph**         | Hard       | [🔗 LeetCode](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph)        |
| 6  | **505. The Maze II**                                 | Medium     | [🔗 LeetCode](https://leetcode.com/problems/the-maze-ii)                                |
| 7  | **1631. Path With Minimum Effort**                   | Medium     | [🔗 LeetCode](https://leetcode.com/problems/path-with-minimum-effort)                   |
| 8  | **2290. Minimum Obstacle Removal to Reach Corner**   | Hard       | [🔗 LeetCode](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner)   |
| 9  | **2642. Design Graph With Shortest Path Calculator** | Hard       | [🔗 LeetCode](https://leetcode.com/problems/design-graph-with-shortest-path-calculator) |
| 10 | **2045. Second Minimum Time to Reach Destination**   | Hard       | [🔗 LeetCode](https://leetcode.com/problems/second-minimum-time-to-reach-destination)   |


"""


from collections import defaultdict
import heapq
from heapq import heappop, heappush
from typing import List

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue  # Already found a better path

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist


"""
This is a variation of dijsktra which can maximize the minimum cost path
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]):
        n = len(grid)
        visited = set()
        pq = [(grid[0][0], 0, 0)]

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while pq:
            t, r, c = heappop(pq)
            if r == n-1 and c == n-1:
                return t
            for dr, dc in dirs:
                x, y = dr+r, dc+c
                if x in range(n) and y in range(n) and (x, y) not in visited:
                    visited.add((x, y))
                    heappush(pq, (max(t, grid[x][y]), x, y))



"""
**Variation**
Intuition:
This is a shortest path problem (minimize cost),
but with an added constraint:
You can only take paths with ≤ k stops.
You can't use plain Dijkstra because Dijkstra assumes:
Once a node is visited with the shortest cost, you can ignore other paths to it.
But in this case:
A cheaper path to a node with more stops may be invalid.
A more expensive path to the same node with fewer stops might be valid.
So, we need to track both cost and number of stops.
"""
# cheapest flight within K-stops
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # Min-heap: (total_cost_so_far, current_node, stops_used)
        pq = [(0, src, 0)]

        # visited[i] = minimum number of stops used to reach node i
        visited = [float('inf')] * n

        while pq:
            cost, u, stops = heappop(pq)

            # Found destination within allowed stops
            if u == dst:
                return cost

            # Prune if stops exceed k or if this path is worse than before
            if stops > k or stops > visited[u]:
                continue

            visited[u] = stops

            # Explore neighbors
            for v, w in graph[u]:
                heappush(pq, (cost + w, v, stops + 1))

        return -1