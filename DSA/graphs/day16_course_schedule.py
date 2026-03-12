class SOlutions:
    def canFinish(self,numCourses,prerequisites):
        graph={i:[] for i in range(numCourses)}
        for course,prereq in prerequisites:
            graph[prereq].append(course)
        state=[0]*numCourses
        def dfs(node):
            if state[node]==1:
                return False
            if state[node]==2:
                return True
            state[node]=1
            for nighbor in graph[node]:
                if not dfs(nighbor):
                    return False
            state[node]=2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True