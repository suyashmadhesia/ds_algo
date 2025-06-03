
from collections import defaultdict, deque
from typing import List

class BFS:
    def multiSourceBFS(self, grid: List[List[int]]) -> None:
        """
        Questions solve using MSB => Rotten Oranges, Island and treasure
        
        Mutates `grid` IN-PLACE.

        Each cell contains one of three values:
        ─  0  :   a *source*  (distance = 0, e.g. a gate, a hospital, a rotten orange, etc.)
        ─ -1  :   a wall / obstacle  (cannot be crossed)
        ─ INF :   an empty room / fresh item that we must fill with its
                  minimum distance to the nearest source

        After the call every INF cell is replaced by its smallest
        Manhattan distance (4-dir) to the *nearest* 0.

        Classic interview problem usually known as “Walls and Gates”.
        -----------------------------------------------------------------
        Multi-Source BFS idea:
        1.  Enqueue **all** sources (all 0-cells) with distance 0.
        2.  Pop cells layer-by-layer; the first time we visit a cell
            we’ve found the shortest path from the *closest* source.
        3.  Update its distance = parent distance + 1 and push it.
        4.  Repeat until queue is empty.
        -----------------------------------------------------------------
        Time  :  O(rows * cols)  (each cell enqueued at most once)
        Space :  O(rows * cols)  (queue + visited)  — can drop `visited`
                                  by re-using the grid as a marker.
        """
        rows = len(grid)
        cols = len(grid[0])
        INF  = 2**31 - 1             # sentinel value for “unreached”

        q = deque()                  # BFS frontier
        visited = set()              # keeps us from enqueuing twice
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]   # 4-direction moves

        # -------------------------------------------------------------
        # 1) INITIALISE QUEUE WITH *ALL* SOURCES (multi-source!)
        # -------------------------------------------------------------
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:          # found a source
                    q.append((r, c))         # distance already 0
                    visited.add((r, c))      # mark as seen

        # -------------------------------------------------------------
        # 2) STANDARD BFS
        # -------------------------------------------------------------
        while q:
            r, c = q.popleft()               # current cell

            # Explore its four neighbours
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                # Check grid bounds
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                # Skip walls and already-visited cells
                if grid[nr][nc] == -1 or (nr, nc) in visited:
                    continue

                # Only update cells that are still INF
                if grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1   # distance = parent + 1
                    q.append((nr, nc))              # push for further expansion
                    visited.add((nr, nc))           # mark so we never push again        rows = len(grid)




"""
0-1 BFS (Zero-One Breadth-First Search) is a specialized version of the Breadth-First Search (BFS) algorithm, used to find the shortest path in a graph where edge weights are only 0 or 1.

🔍 When to Use 0-1 BFS
Use 0-1 BFS when:
The graph is unweighted but with implicit weights of 0 and 1.
Edge weights are either 0 or 1.

You need efficient shortest path computation (faster than Dijkstra's).

Steps:

1. If an edge has weight 0, insert the destination node at the front of the deque.
2. If an edge has weight 1, insert it at the back of the deque.



🧠 Time Complexity
O(V + E) — where V is the number of vertices and E is the number of edges.

✅ Example Use Case
Suppose you’re moving in a grid where moving to an adjacent cell costs 0 if the cell is empty, and 1 if it contains an obstacle that can be removed. 0-1 BFS helps efficiently compute the minimal cost path.

Problem Example:
1. Find Safe walk through a grid https://leetcode.com/problems/find-a-safe-walk-through-a-grid/
2. Minimum Obstacle Removal to Reach Corner https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
"""

def zero_one_bfs(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    dq = deque([start])

    while dq:
        node = dq.popleft()
        for neighbor, weight in graph[node]:
            if dist[neighbor] > dist[node] + weight:
                dist[neighbor] = dist[node] + weight
                if weight == 0:
                    dq.appendleft(neighbor)
                else:
                    dq.append(neighbor)

    return dist

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # 0 1 DFS problem (similar to dijkstra)
        graph = defaultdict(list)
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                for dr, dc in dirs:
                    r, c = dr+i, dc+j
                    if (r in range(m)) and (c in range(n)):
                        graph[i, j].append((grid[r][c], (r, c)))
        
        costs = [[float('inf') for _ in range(n)] for _ in range(m)]
        costs[0][0] = grid[0][0]

        q = deque([(grid[0][0] ,(0, 0))])
        while q:
            curr_cost, node = q.popleft()
            r, c = node
            if r == m-1 and c == n-1 and curr_cost < health:
                return True
            for cost, nei in graph[node]:
                if costs[r][c]+cost < costs[nei[0]][nei[1]] and costs[r][c]+cost < health:
                    # just update the current health after traversing the shell
                    # if current health drops to zero then we will try to procced
                    costs[nei[0]][nei[1]] = costs[r][c]+cost
                    if cost == 0:
                        q.appendleft((costs[r][c]+cost, nei))
                    else:
                        q.append((costs[r][c]+cost, nei))
        
        return False

        