"""

Finding de Bruijn Sequence using Eulerian Circuit (hierholzer's Algorithm)
You use a graph-based approach where:
Nodes represent strings of length n-1
Edges represent transitions (adding a new character) → each edge corresponds to a string of length n
The goal is to find an Eulerian circuit in this graph:
One that visits every edge exactly once
This guarantees each n-length string appears exactly once

🛠️ Step-by-Step Construction
Step 1: Generate Alphabet
    For k = 2, the alphabet is ['0', '1']

Step 2: Build the De Bruijn Graph
    Each node is a string of length n - 1
    For each node, connect it to all possible nodes by shifting + appending one character
    Example for n = 3, k = 2:
    Nodes: "00", "01", "10", "11"
    Edge from "00" → "01" represents the string "001"
    We store this as:
    graph["00"] = ["00", "01"] (from "00" + "0" and "00" + "1" → "000", "001")

Step 3: Find Eulerian Circuit
    Use Hierholzer's Algorithm
    Start DFS from a valid start node
    Always go deep until stuck, then backtrack and build the path
    This ensures each edge (i.e., each n-length string) is visited once

Step 4: Reconstruct the De Bruijn Sequence
    Use the Eulerian circuit
    First node is the prefix
    From then on, add only the last character of each new node

"""

from collections import defaultdict, deque

n = int(input("Enter range: "))
k = int(input("Enter size: "))

from collections import defaultdict

# Input
n = int(input("Enter n (length of substrings): "))
k = int(input("Enter k (alphabet size): "))

# Step 1: Generate the alphabet (e.g., ['0', '1'] for binary)
alphabet = [str(i) for i in range(k)]

# Step 2: Build the De Bruijn graph
graph = defaultdict(list)

def build_graph(node):
    """
    For each node (length n-1), add edges by appending each alphabet character.
    Edge goes to the last n-1 chars after appending.
    """
    for ch in alphabet:
        edge = node + ch
        if n == 1:
            graph[node].append(ch)
        else:
            graph[node].append(edge[1:])  # simulate shift

def generate_nodes(node):
    """
    Generate all possible nodes (strings of length n-1) recursively.
    Base case: when node is of length n-1, create edges for it.
    """
    if len(node) == n - 1:
        build_graph(node)
        return
    for ch in alphabet:
        generate_nodes(node + ch)

# iterative method for generating the nodes
def generate_nodes_iterative():
    """
    Generate all possible nodes (strings of length n-1) iteratively.
    For each node, build the outgoing edges.
    """
    queue = deque([""])  # Start with empty string

    while queue:
        current = queue.popleft()
        if len(current) == n - 1:
            build_graph(current)
        else:
            for ch in alphabet:
                queue.append(current + ch)

# Start recursive node generation
generate_nodes("")  # starts with empty string

# Step 3: Hierholzer's Algorithm to find Eulerian circuit
circuit = []

def dfs(u):
    """
    Recursively visit edges using DFS.
    When a node has no further edges, append it to the circuit.
    This builds the Eulerian path in reverse.
    """
    while graph[u]:
        v = graph[u].pop()  # remove edge u → v
        dfs(v)
    circuit.append(u)  # backtracking step

# Start node for Eulerian circuit
start_node = alphabet[0] * (n - 1) if n > 1 else ''  # e.g., "00" or ""

# Perform DFS from the starting node
dfs(start_node)

# Step 4: Reconstruct the De Bruijn sequence from Eulerian circuit
circuit = circuit[::-1]  # reverse the path to get correct order
sequence = circuit[0]    # first node is the base

# For remaining nodes, only append the last character
for node in circuit[1:]:
    if node:  # avoid empty nodes (possible if n = 1)
        sequence += node[-1]

print("De'Bruijn Sequence:", sequence)
