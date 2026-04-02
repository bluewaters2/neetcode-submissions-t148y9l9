class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque()
        ans =  []

        for i, num in enumerate(indegree):
            if num == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            ans.append(node)
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)
        
        for i, num in enumerate(indegree):
            if num > 0:
                return []
        
        return ans