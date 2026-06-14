class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visit = set()
        cnt = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):

            
            if not (0<=i<m and 0<=j<n and grid[i][j]=="1"):
                return  
            
            grid[i][j]='0'
            
            dirs =[(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in dirs:
                dfs(i+dr, j+dc)  

        for i in range(m):
            for j in range(n):
                if  grid[i][j]=="1":
                    
                    dfs(i,j)
                    cnt+=1
        return cnt
        