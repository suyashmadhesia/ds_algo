def topo_sort(n, edges):
    """
    Perform a topological sort on a directed graph with n nodes (0 to n-1)
    and given list of directed edges.

    Returns:
        A list of nodes in topologically sorted order if no cycle exists,
        otherwise an empty list.
    """
    # 'visited' keeps track of nodes in the current DFS recursion stack (for cycle detection)
    visited = set()
    # 'added' keeps track of nodes that have been fully processed and added to result
    added = set()
    # build adjacency list: for each u -> list of v's
    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)

    res = []  # will hold nodes in reverse topological order

    def dfs(cur):
        """
        Depth-first search that returns False if a cycle is detected,
        otherwise True. Upon finishing exploring all descendants of 'cur',
        it appends 'cur' to 'res'.
        """
        # If 'cur' is in visited, we found a back-edge → cycle
        if cur in visited:
            return False
        # If already fully processed, no need to do it again
        if cur in added:
            return True

        # Mark 'cur' as being visited in this path
        visited.add(cur)
        # Recurse on all outgoing edges
        for neighbor in adj[cur]:
            if not dfs(neighbor):
                return False  # propagate cycle detection
        # Done exploring all descendants of 'cur'
        visited.remove(cur)  # backtrack: remove from current recursion stack
        added.add(cur)       # mark as fully processed
        res.append(cur)      # append to result (post-order)

        return True

    # Run DFS from every node (to cover disconnected components)
    for node in range(n):
        if not dfs(node):
            return []  # cycle detected → no valid topological ordering

    # 'res' is in reverse topological order: the last finished node is first in order
    return res[::-1]  # reverse it to get correct topological order


print(topo_sort(4, [[1,0],[2,0],[3,1],[3,2]]))