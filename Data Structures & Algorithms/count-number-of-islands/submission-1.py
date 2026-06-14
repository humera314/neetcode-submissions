class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row= len(grid)

        col = len(grid[0])

        count=0
        def dfs(r,c):
            dirs=[(0,1), (1,0), (-1,0), (0,-1)]
            if 0>r or r>=row or 0>c or c>=col or grid[r][c]=='0':
                    return

            grid[r][c]='0'

            for nr, nc in dirs:
                dfs(r+nr, c+nc)
                
        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1':
                    dfs(r,c)
                    count+=1
        return count

        