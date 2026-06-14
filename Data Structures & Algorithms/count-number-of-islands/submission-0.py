import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()  # Set to track visited cells
        island = 0  # To count the number of islands
        row, col = len(grid), len(grid[0])  # Get number of rows and columns in the grid

        # Define BFS function for traversing the grid
        def bfs(r, c):
            print(f"Starting BFS at ({r}, {c})")  # Debug: Print starting point of BFS
            # Directions to move in 4 directions (right, left, down, up)
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            q = collections.deque()  # Queue for BFS
            visit.add((r, c))  # Mark the starting cell as visited
            q.append((r, c))  # Add starting point to queue

            # Process the queue
            while q:
                cur_r, cur_c = q.pop()  # Pop the current cell from the queue
                print(f"Visiting cell: ({cur_r}, {cur_c})")  # Debug: Print current cell being processed

                # Explore neighbors
                for dr, dc in directions:
                    new_r, new_c = cur_r + dr, cur_c + dc  # Calculate the new position
                    # Check if the new position is within bounds and if it's a land cell ('1')
                    if 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) not in visit and grid[new_r][new_c] == '1':
                        print(f"Adding ({new_r}, {new_c}) to queue")  # Debug: Print the neighbor being added to queue
                        # visit.add((new_r, new_c))  # Mark the neighbor as visited
                        # q.append((new_r, new_c))  # Add neighbor to the queue    BFSSSS
                        bfs(new_r,new_c)

        # Loop through each cell in the grid
        for r in range(row):
            for c in range(col):
                # Start BFS for every unvisited land cell ('1')
                if grid[r][c] == "1" and (r, c) not in visit:
                    print(f"New island found at ({r}, {c})")  # Debug: Print when a new island is found
                    bfs(r, c)  # Call BFS to visit the entire island
                    island += 1  # Increment island count after BFS

        # Return the total number of islands
        print(f"Total number of islands: {island}")  # Debug: Print final island count
        return island
