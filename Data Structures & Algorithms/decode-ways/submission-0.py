class Solution:
    def numDecodings(self, s: str) -> int:
        dp={len(s):1}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            
            if s[i]=="0": # for starting with 0
                return 0

            print("HOW FORST")
            res=dfs(i+1)
            print("when")

            if i+1 < len(s) and (s[i]=='1' or s[i]=='2' and s[i+1] in '0123456'):
                res+=dfs(i+2)
            dp[i]=res
            print('are u printing')
            return res
        
        
        return dfs(0)