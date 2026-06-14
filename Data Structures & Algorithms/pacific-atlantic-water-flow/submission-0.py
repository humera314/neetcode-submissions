class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific=set()
        atlantic=set()

        visit= set()

        rows=len(heights)
        cols=len(heights[0])
        
        output=[]
        print(cols, rows)
        
        def dfs(r, c, visit, prev):
            if ((r,c) in visit or
                r<0 or c< 0 or r==rows 
                or c== cols or heights[r][c] < prev):
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c]) 
            dfs(r-1, c, visit, heights[r][c])   
            dfs(r, c+1, visit, heights[r][c])    
            dfs(r, c-1, visit, heights[r][c])  


        for left in range(cols):
            dfs(0, left, pacific, heights[0][left])  
            dfs(rows-1,left,atlantic, heights[rows-1][left])  
    
        for top in range(rows):
            dfs(top,0, pacific, heights[top][0])  
            dfs(top,cols-1,atlantic, heights[top][cols-1])  
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    output.append([r,c])
        return output


        