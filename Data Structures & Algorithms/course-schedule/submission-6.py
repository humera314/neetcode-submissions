from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[course].append(pre)

        visit = set()      # fully processed nodes
        path = set()       # current DFS path

        def dfs(course):

            if course in path:      # cycle found
                return True

            if course in visit:     # already checked
                return False

            path.add(course)

            for pre in adj[course]:
                if dfs(pre):
                    return True

            path.remove(course)
            visit.add(course)

            return False

        for course in range(numCourses):
            if dfs(course):
                return False

        return True