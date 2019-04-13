numCourses=5
graph = [[] for _ in range(numCourses)]
print(graph)
visit = [0 for _ in range(numCourses)]
print(visit)

prerequisites=[[1,0],[2,0],[3,2],[4,3],[4,2]]
for x, y in prerequisites:
    graph[x].append(y)
print(graph)
print(visit)

for j in []:
    print(j)

class Solution:
    def canFinish(self,numCourses,prerequisites):
        graph=[[] for _ in range(numCourses)]
        visit=[0 for _ in range(numCourses)]
        for x,y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i]==-1:
                return False
            if visit[i]==1:
                return True
            visit[i]=-1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i]=1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

S=Solution()
print(S.canFinish(numCourses,prerequisites))