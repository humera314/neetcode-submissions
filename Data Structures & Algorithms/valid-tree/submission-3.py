class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj=[[] for _ in range(n)]
        visit=set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)

            for ngbr in adj[node]:
                if ngbr==par:
                    continue
                if not dfs(ngbr, node):
                    return False
            return True

        return dfs(0,-1) and len(visit)==n