from typing import List
import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            print("Empty grid. Nothing to do.")
            return 
        
        row, col = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = collections.deque()

        print("Initial Grid:")
        for r in grid:
            print(r)

        # Enqueue all gates (cells with 0)
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r, c))
                    print(f"Gate found at ({r}, {c})")

        print("\nStarting BFS...\n")

        # BFS from all gates
        while q:
            cur_r, cur_c = q.popleft()
            print(f"Processing cell ({cur_r}, {cur_c}) with value {grid[cur_r][cur_c]}")
            
            for dr, dc in dirs:
                new_r, new_c = cur_r + dr, cur_c + dc
                if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 2147483647:
                    grid[new_r][new_c] = grid[cur_r][cur_c] + 1
                    print(f"Updated neighbor ({new_r}, {new_c}) to {grid[new_r][new_c]}")
                    q.append((new_r, new_c))

        print("\nFinal Grid with Distances:")
        for r in grid:
            print(r)
