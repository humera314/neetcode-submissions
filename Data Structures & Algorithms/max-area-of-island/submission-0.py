class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        maxArea=0
        row, col= len(grid), len(grid[0])

        def bfs(r,c,maxArea):
            dir=[(0,1),(0,-1),(1,0),(-1,0)]
            q=collections.deque()
            visited.add((r,c))
            area=1
            q.append((r,c))
            while q:
                cur_r,cur_c=q.popleft()
                for dr,dc in dir:
                    new_r,new_c= cur_r+dr, cur_c+dc
                    if 0<=new_r<row and 0<=new_c<col and (new_r,new_c) not in visited and grid[new_r][new_c]==1:
                        area+=1
                        
                        visited.add((new_r,new_c))
                        q.append((new_r,new_c))
            return area




        for r in range(row):
            for c in range(col):
                if grid[r][c]==1 and (r,c) not in visited:
                    curArea=bfs(r,c,maxArea)
                    maxArea=max(curArea, maxArea)
        return maxArea
     

        