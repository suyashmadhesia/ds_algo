"""
Kahn's Algorithm for finding topological sort of a graph

🔧 Key Concepts:
In-degree of a node: Number of edges coming into it.
Nodes with in-degree 0 can be visited first.
Remove such nodes from the graph and reduce the in-degree of their neighbors.
Repeat until all nodes are visited.

🧠 Intuition:
Think of tasks that have dependencies. You can only start a task if all its dependencies are done. Kahn's algorithm is just that:
→ Start with tasks that have no dependencies (in-degree 0),
→ Complete them,
→ Then move to tasks that now have all dependencies met.

🧩 Step-by-Step Algorithm:
1. Let’s say the graph has V vertices.
2. Compute in-degree for every node.
3. Push all nodes with in-degree 0 into a queue.
4. While queue is not empty:
5. Pop a node.
6. Add it to the result (topological order).
7. For each neighbor:
8. Decrease its in-degree by 1.
9. If in-degree becomes 0, push it into the queue.
10. If the result has fewer nodes than V, there's a cycle (no topological ordering possible).

🧮 Time & Space Complexity:
Time: O(V + E)
(You process each node and each edge once.)

Space: O(V + E)
(For storing graph + in-degree + queue.)

"""

from collections import deque


def kahsBFS(n, edges):

    degree = [0] * n

    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        degree[v] = -~degree[v]

    q = deque([i for i in range(n) if degree[i] == 0])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for neighbor in adj[node]:
            degree[neighbor]-=1
            if degree[neighbor] == 0:
                q.append(neighbor)
    
    if len(order) ==n:
        print(order[::-1]) # this is correct order for traversing the topological graph
        return
    print([])


kahsBFS(2, [[1,0],[0,1]])

    