class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj=[[] for _ in range(numCourses)]
        visit=set()
        for u,v in prerequisites:
            adj[u].append(v)
        

        def isCycle(node):
            if node in visit:
                return False
            if adj[node]==[]:
                
                return True
            visit.add(node)

            for ngbr in adj[node]:
                if not isCycle(ngbr):
                    return False
            
            visit.remove(node)
            adj[node]=[]

            return True
            


        for i in range(numCourses):
            if not isCycle(i):
                return False
        return True