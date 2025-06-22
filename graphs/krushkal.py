"""
---

## 🚩 What is Kruskal's Algorithm?

* **Goal**: To find the **Minimum Spanning Tree (MST)** — a subset of edges that connects all vertices with the **minimum possible total edge weight** and **no cycles**.
* **Approach**: Sort all the edges and **pick the smallest edge** that doesn't form a **cycle**.
* Uses the **Disjoint Set Union (DSU)** or **Union-Find** data structure to detect cycles.

---

## 🧠 Intuition Behind Kruskal’s Algorithm

1. **Greedy Choice**: Always pick the smallest edge available.
2. **Avoid Cycles**: We only add edges if they **do not connect vertices already in the same set** (i.e., they won’t form a cycle).
3. **Continue Until** we have added exactly `V-1` edges (`V` is the number of vertices).

---

## 🏗️ Data Structures Used

### 1. **Edge List**:

* Store edges as `(weight, u, v)`

### 2. **DSU (Disjoint Set Union)**:

* Helps check whether two vertices are already connected.
* Two operations:

  * `find(u)`: returns the root of the set `u` belongs to.
  * `union(u, v)`: merges sets containing `u` and `v`.

---

## 🔁 Kruskal’s Algorithm Steps

### Given: `n` nodes and `edges` list of form `(u, v, weight)`

### Step-by-Step:

1. **Sort all edges by weight** (ascending).
2. **Initialize DSU**: each node is its own parent initially.
3. **Initialize MST Weight = 0 and MST Edges = \[]**
4. **Iterate through sorted edges**:

   * If `u` and `v` are in **different sets** (i.e., `find(u) != find(v)`):

     * Add edge to MST.
     * Merge sets (`union(u, v)`).
     * Add edge weight to total.
5. Stop when we have `n - 1` edges in MST.
## 🧪 Example

```python
n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
```

### Step-by-step:

1. Sort edges:
   ```
   (2, 3, 4)
   (0, 3, 5)
   (0, 2, 6)
   (0, 1, 10)
   (1, 3, 15)
   ```

2. Add (2, 3, 4) → OK (no cycle)
3. Add (0, 3, 5) → OK
4. Add (0, 2, 6) → Cycle! (already connected)
5. Add (0, 1, 10) → OK

### MST: `[(2, 3, 4), (0, 3, 5), (0, 1, 10)]`

* Total weight = `4 + 5 + 10 = 19`

---

## ⏱️ Time Complexity

* **Sorting edges**: `O(E log E)`
* **DSU operations**: nearly constant (`O(α(N))`)
* **Overall**: `O(E log E)` where `E` = number of edges

---

## 📌 Key Points to Remember

* Kruskal’s works best for **sparse graphs** (less edges).
* Always **sort edges first**.
* Use **Union-Find** to detect cycles.
* Resulting MST will have **V-1 edges**.

---
"""



## 📦 Kruskal’s Algorithm in Python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False  # Cycle
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True

def kruskal(n, edges):
    # Step 1: Sort edges by weight
    edges.sort(key=lambda x: x[2])  # (u, v, weight)

    dsu = DSU(n)
    mst_weight = 0
    mst_edges = []

    # Step 2: Loop through sorted edges
    for u, v, weight in edges:
        if dsu.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
            if len(mst_edges) == n - 1:
                break

    return mst_weight, mst_edges
