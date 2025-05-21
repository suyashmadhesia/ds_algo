from typing import List
from collections import deque

class Solution:
    """
    How DFS detects a cycle in an undirected graph
    In DFS traversal:
    When visiting a node, you recursively explore all its unvisited neighbors.
    If you encounter a node that is already visited and is not the parent of the current node, it means there is a back edge, which forms a cycle.
    This method works because in an undirected graph, edges go both ways — so we must ignore the edge that goes back to the immediate parent.
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Step 1: Build the adjacency list for an undirected graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # Add the reverse edge for undirected graph

        visited = set()  # To keep track of visited nodes

        def dfs(node, parent):
            """
            Performs DFS to detect cycle.
            - node: current node being visited
            - parent: node we came from, used to avoid false positives
            """
            if node in visited:
                return False  # Cycle detected

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Skip the parent node (edge we came from)

                if not dfs(neighbor, node):
                    return False  # If a cycle is found in recursion

            return True  # No cycles detected from this path

        # Step 2: Start DFS from node 0
        # - Check for cycle (dfs returns False if there is one)
        # - Also check that all nodes are visited (i.e., graph is connected)
        return dfs(0, -1) and len(visited) == n
    

    def validTreeBFS(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        q = deque([(0, -1)])  # (current node, parent node)
        visit.add(0)
        
        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))
        
        return len(visit) == n