class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj={i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit=[False] * n

        def dfs(i):
            for nei in adj[i]:
                if not visit[nei]:
                    visit[nei]= True
                    dfs(nei)

        res=0
        for node in range(n):
            if not visit[node]:
                visit[node]=True
                dfs(node)
                res+=1
        return res

        