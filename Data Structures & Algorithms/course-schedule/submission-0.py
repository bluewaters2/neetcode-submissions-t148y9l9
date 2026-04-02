# Plan
# we can use topological sorting to check whether it is possible to finish all the courses
# we have an indegree array to keep track of all the courses you are required to take


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for i, num in enumerate(indegree):
            if num == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)
        
        for num in indegree:
            if num > 0:
                return False
        
        return True