class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()  # Set to track visited cells
        maxArea = 0  # Maximum area of island
        row, col = len(grid), len(grid[0])  # Number of rows and columns

        def bfs(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up directions
            q = collections.deque()
            visited.add((r, c))  # Mark the starting cell as visited
            area = 1  # The area of the island (starting with the current cell)
            q.append((r, c))
            print(f"Starting BFS from ({r}, {c})")

            while q:
                cur_r, cur_c = q.popleft()  # Pop the leftmost element from the queue
                print(f"Visiting cell ({cur_r}, {cur_c})")
                
                for dr, dc in directions:
                    new_r, new_c = cur_r + dr, cur_c + dc
                    # Check if the new cell is within bounds, not visited, and is land (1)
                    if 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) not in visited and grid[new_r][new_c] == 1:
                        area += 1  # Increment the area
                        visited.add((new_r, new_c))  # Mark the new cell as visited
                        q.append((new_r, new_c))  # Add the new cell to the queue
                        print(f"Adding cell ({new_r}, {new_c}) to queue, current island area: {area}")
            print(f"Finished BFS from ({r}, {c}), island area: {area}")
            return area  # Return the area of the island

        # Loop through the grid to find all islands
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    print(f"Starting new island search at ({r}, {c})")
                    curArea = bfs(r, c)  # Find the area of the island starting from (r, c)
                    maxArea = max(curArea, maxArea)  # Update the max area if needed
                    print(f"Max area updated: {maxArea}")

        print(f"Maximum area of an island: {maxArea}")
        return maxArea  # Return the largest island area
