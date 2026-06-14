class Solution:
    def climbStairs(self, n: int) -> int:

        def dp(n):
            if n==0:
                return
            if n==1:
                return 1
            if n == 2:
                return 2

            return( dp(n-1)+ dp(n-2))
        return dp(n)