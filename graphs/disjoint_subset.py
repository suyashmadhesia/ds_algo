class DSU:

    def __init__(self, nodes: int):
        self.parent = list(range(nodes))

    def union(self, node):
        x, y = node
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Cycle detected
        self.parent[py] = px
        return True
        


    def find(self, node):
        # Path compression with while loop
        root = node
        while self.parent[root] != root:
            root = self.parent[root]
        
        # Optional path compression
        while node != root:
            parent = self.parent[node]
            self.parent[node] = root
            node = parent

        return root
    
dsu = DSU(5)
dsu.union((0, 1))
dsu.union((1, 2))
dsu.union((2, 3))
dsu.union((3, 4))

print(dsu.parent)

# def has_cycle(n, edges):
#     dsu = DSU(n)
#     for u, v in edges:
#         if not dsu.union(u, v):
#             return True  # Found a cycle
#     return False

# has_cycle(8)
