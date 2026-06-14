class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        course={i:[] for i in range(numCourses)}
        visit=set()

        for u,v in prerequisites:
            course[v].append(u)

        def dfs(num):
            if num in visit:
                return False
            if course[num]==[]:
                return True

            visit.add(num)
            for ngbr in course[num]:
                if not dfs(ngbr):
                    return False
            visit.remove(num)
            course[num]=[]
            return True

            
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        