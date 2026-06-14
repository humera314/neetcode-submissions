class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(val):
            if val<0:
                return 0
            if val==1 or val==2:
                return val
            return dfs(val-1) + dfs(val-2) 
        return dfs(n)
        