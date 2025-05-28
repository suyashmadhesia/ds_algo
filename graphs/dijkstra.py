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


import heapq

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
