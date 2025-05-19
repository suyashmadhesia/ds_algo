
from collections import deque
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