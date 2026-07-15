class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visit = set()
        adj = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        def dfs(cur):
            if cur in visit:
                return False
            if adj[cur] == []:
                return True
            visit.add(cur)
            for nei in adj[cur]:
                if not dfs(nei) : return False
            visit.remove(cur)
            adj[cur] = []
            return True
        for i in range(numCourses):
            if not dfs(i) : return False
        return True

            
