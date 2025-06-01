"""

# 🧠 Hierholzer’s Algorithm (General Version)

## 🔍 Goal:

Find an Eulerian circuit or Eulerian path in a graph:

 An Eulerian circuit visits every edge exactly once and returns to the starting vertex.
 An Eulerian path visits every edge exactly once, but does not have to return to the start.

---

## ✅ Conditions to Use:

### For Undirected Graphs:

 Eulerian Circuit: All vertices have even degree and the graph is connected.
 Eulerian Path: Exactly 0 or 2 vertices have odd degree and the graph is connected.

### For Directed Graphs:

 Eulerian Circuit: Every vertex has equal in-degree and out-degree, and the graph is strongly connected.
 Eulerian Path: Exactly one vertex has out-degree = in-degree + 1  (start point), and one has in-degree = out-degree + 1 (end point). All others must have equal in-degree/out-degree.

---

## 🔧 Algorithm Steps (General Idea):

### Step 1: Pre-check

 Validate Eulerian path/circuit conditions (see above).

### Step 2: Build Graph Representation

 Use adjacency list or dict (support multiedges if needed).

### Step 3: DFS Traversal (Post-order)

1. Start from the start vertex:

    For Eulerian circuit, any vertex with non-zero degree.
    For Eulerian path, the special start vertex (with out-degree = in-degree + 1).
2. Use DFS, and:

    While there are unused edges from current vertex:

      Pick any (e.g., lex smallest) edge.
      Remove edge (mark as visited or pop).
      Recurse on that edge’s target.
    Once stuck (no outgoing edges left), add vertex to path.
3. Finally, reverse the path.

---

## 🧮 Time Complexity:

 O(E) if adjacency list used
 O(E log D) if heap used for lex order (where D = max degree)

---


```

---

## 🧪 Example (Undirected):

Graph:

```
A -- B
|    |
C -- D
```

Adjacency list:

```python
graph = {
  "A": ["B", "C"],
  "B": ["A", "D"],
  "C": ["A", "D"],
  "D": ["B", "C"]
}
```

Resulting circuit:
`A → C → D → B → A`

---

## 🧪 Example (Directed):

Tickets:

```
A → B  
B → C  
C → A
```

Eulerian circuit: `A → B → C → A`

---

## 🧠 Summary of Hierholzer's Algorithm:

| Feature         | Value                            |
| --------------- | -------------------------------- |
| Graph Type      | Directed & Undirected            |
| Handles         | Eulerian Path & Circuit          |
| Works with      | Multigraphs, Loops               |
| Time Complexity | O(E) or O(E log E)               |
| Strategy        | DFS-based, post-order traversal  |
| Output          | Edge-used path from start to end |

---
"""


# undirected graph implementation
from collections import defaultdict


# Determine if an undirected graph has an Eulerian circuit, path, or neither
def is_eulerian_undirected(graph):
    odd = 0  # Count of vertices with odd degree
    for node in graph:
        if len(graph[node]) % 2 != 0:  # Check if degree is odd
            odd += 1
    if odd == 0:
        return "circuit"  # All degrees even → Eulerian Circuit
    elif odd == 2:
        return "path"     # Exactly two odd degrees → Eulerian Path
    else:
        return None       # More than two odd degrees → Neither

# Choose a starting point for the Eulerian trail
def find_start_undirected(graph):
    # If Eulerian path: start from a vertex with odd degree
    for node in graph:
        if len(graph[node]) % 2 != 0:
            return node
    # Else for Eulerian circuit: start from any vertex with non-zero degree
    for node in graph:
        if graph[node]:
            return node
    return None


# Main Hierholzer's Algorithm for undirected graph
def hierholzer_undirected(graph_input):
    graph = defaultdict(list)
    
    # Build the adjacency list (since it's undirected, add both directions)
    for u, v in graph_input:
        graph[u].append(v)
        graph[v].append(u)

    status = is_eulerian_undirected(graph)  # Check if Eulerian path/circuit exists
    if not status:
        return "No Eulerian Path or Circuit"

    start = find_start_undirected(graph)  # Find suitable starting node
    circuit = []  # Result path

    # Recursive DFS function to construct the Eulerian path/circuit
    def dfs(u):
        while graph[u]:  # While edges are available from `u`
            v = graph[u].pop()  # Remove one neighbor
            graph[v].remove(u)  # Remove reverse edge (since undirected)
            dfs(v)  # Continue DFS from neighbor
        circuit.append(u)  # Append to result after exploring all edges

    dfs(start)
    return circuit[::-1]  # Reverse because we backtrack at the end



# directed graph implementation

# Determine if the graph has a Eulerian path or circuit (directed)
def is_eulerian_directed(graph):
    in_deg = defaultdict(int)   # Track in-degrees
    out_deg = defaultdict(int)  # Track out-degrees

    # Count in-degrees and out-degrees
    for u in graph:
        for v in graph[u]:
            out_deg[u] += 1
            in_deg[v] += 1

    start_nodes = end_nodes = 0  # To track path start and end candidates

    for node in set(list(in_deg.keys()) + list(out_deg.keys())):
        # Case: possible start of Euler path (out-degree = in-degree + 1)
        if out_deg[node] - in_deg[node] == 1:
            start_nodes += 1
            start = node
        # Case: possible end of Euler path (in-degree = out-degree + 1)
        elif in_deg[node] - out_deg[node] == 1:
            end_nodes += 1
        # Otherwise, degrees must be exactly equal
        elif in_deg[node] != out_deg[node]:
            return None, None  # Invalid

    # Eulerian Circuit (all in-deg == out-deg)
    if start_nodes == 0 and end_nodes == 0:
        for node in graph:
            if graph[node]:  # Start from any node with an outgoing edge
                return "circuit", node

    # Eulerian Path (1 start, 1 end)
    elif start_nodes == 1 and end_nodes == 1:
        return "path", start

    return None, None  # Otherwise, no Eulerian trail

# Main Hierholzer’s Algorithm for directed graph
def hierholzer_directed(graph_input):
    graph = defaultdict(list)

    # Build the adjacency list
    for u, v in graph_input:
        graph[u].append(v)

    # Optional: sort in reverse order if you need lexicographically smallest path
    for u in graph:
        graph[u].sort(reverse=True)

    status, start = is_eulerian_directed(graph)  # Validate graph type
    if not status:
        return "No Eulerian Path or Circuit"

    circuit = []  # Result path

    # Recursive DFS
    def dfs(u):
        while graph[u]:  # While there are outgoing edges from `u`
            v = graph[u].pop()  # Pop the last neighbor (rightmost for lex min)
            dfs(v)  # Continue from `v`
        circuit.append(u)  # Add current node after all edges are explored

    dfs(start)
    return circuit[::-1]  # Reverse the result path
