from typing import List, Tuple, Set, Generator

def dfs(node, neighbors_fn, visited, process_fn=None):
    """
    A generic depth-first search.

    Args:
      node:         The current node (of any hashable type).
      neighbors_fn: A function f(node) → iterable of neighbor-nodes.
      visited:      A set to track which nodes have been seen.
      process_fn:   Optional function f(node) → value to accumulate or side-effect.

    Returns:
      If process_fn returns numeric contributions, you could sum them; 
      otherwise, returns None and relies on side-effects.
    """
    # Base case: already visited
    if node in visited:
        return 0 if process_fn else None

    # Mark as visited
    visited.add(node)

    # “Process” this node (e.g. count it, record it, etc.)
    count = process_fn(node) if process_fn else None

    # Recurse on all neighbors
    for nbr in neighbors_fn(node):
        result = dfs(nbr, neighbors_fn, visited, process_fn)
        if count is not None and result is not None:
            count += result

    return count


"""

Example is Max of Island area

"""



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited: Set[Tuple[int,int]] = set()
        
        # 1) Define how to get neighbors in the grid
        def grid_neighbors(cell: Tuple[int,int]) -> Generator[Tuple[int,int]]:
            r, c = cell
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    yield (nr, nc)
        
        # 2) Define how to “process” each node: count it as 1
        def count_one(cell: Tuple[int,int]) -> int:
            return 1
        
        max_area = 0
        # 3) Iterate over every cell; if it’s unvisited land, launch a DFS
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs((r, c), grid_neighbors, visited, process_fn=count_one)
                    max_area = max(max_area, area)
        
        return max_area


# You still need to include the generic dfs() above in the same module.
# With this structure, you can now swap in ANY graph or grid
# simply by providing a different neighbors_fn and process_fn.
