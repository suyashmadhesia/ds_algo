### ✅ 1. **Divide and Conquer Optimization**
Used to optimize dynamic programming where the recurrence satisfies the **Monotonicity of the Decision Function** (e.g., dp[i][j] = min_k<f(i, j, k)>).

- **Example Use:** [Knuth Optimization](https://en.wikipedia.org/wiki/Knuth_optimization), DP optimizations in O(N log N) or O(N^2).

---

### ✅ 2. **Convex Hull Trick / Line Container**
Used to maintain a set of linear functions to answer minimum/maximum queries efficiently.

- **Use Case:** Optimization over convex functions, DP with linear cost.

---

### ✅ 3. **Suffix Array / Suffix Automaton**
Efficient structures for processing strings:
- O(n log n) for suffix array.
- O(n) for suffix automaton.
  
- **Applications:** LCP queries, string matching, substring counting.

---

### ✅ 4. **Heavy-Light Decomposition (HLD)**
Used for fast queries on tree paths (e.g., sum/max/min from node u to v).

- Works well with segment trees.

---

### ✅ 5. **Centroid Decomposition**
Breaks a tree recursively at centroids, good for divide-and-conquer style approaches on trees.

- **Use Case:** Path counting, distance queries, etc.

---

### ✅ 6. **Mo's Algorithm (Sqrt Decomposition)**
Efficiently processes range queries offline in O((n + q) sqrt n) time.

- **Use Case:** Querying frequency, sum, GCD over subarrays.

---

### ✅ 7. **Binary Lifting**
Used for LCA (Lowest Common Ancestor) and jumping 2^k ancestors up in trees.

- O(log N) per query.

---

### ✅ 8. **Persistent Segment Trees**
Segment trees where every update creates a new version of the tree, allowing time-travel-like queries.

- **Use Case:** Range queries over dynamic arrays, historical lookups.

---

### ✅ 9. **DSU on Tree (a.k.a. small-to-large)**
Optimized DFS method for subtree queries combined with Disjoint Set Union techniques.

- **Use Case:** Counting colors, values, etc. in subtrees.

---

### ✅ 10. **Link-Cut Trees / Euler Tour Trees**
Advanced dynamic trees supporting link/cut and path queries in O(log N).

- Often implemented using **Splay Trees** or **Treaps**.

---

## 📦 Advanced Data Structures

- **Treaps / Splay Trees / AVL Trees** (for dynamic ordered sets/maps)
- **Segment Trees / Fenwick Trees (BIT)** with:
  - Lazy propagation
  - Merge strategies
  - Beats / Advanced variants
- **Binary Trie** (for bit manipulation problems)
- **Wavelet Tree / Merge Sort Tree** (for range k-th smallest/largest queries)
- **K-D Tree** (multi-dimensional search)
- **Hashing + Rolling Hash** (for substring matching)

---

## 📈 Graph Algorithms

- **2-SAT** (Boolean satisfiability)
- **Tarjan’s Algorithm** (SCC, bridge-finding)
- **Kosaraju's Algorithm** (SCC)
- **Johnson's Algorithm** (All-pairs shortest path with negative weights)
- **Min-Cost Max-Flow**
- **Dijkstra + Binary Heap / Dial’s / Fibonacci Heap**
- **Floyd-Warshall + Path Reconstruction**
- **Euler Tour Technique** (flattening trees)

---


## 🔁 Bit Manipulation

- **Bitmask DP**
- **Subset Enumeration using Masks**
- **SOS DP (Sum over Subsets)**

---
