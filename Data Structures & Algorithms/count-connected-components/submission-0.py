# build an adjacency list
# Use dfs and bfs to visit all nodes in a component
# each time a new traversal from an unvisited node indicates a new component
# 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        ans = 0

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n

        q = deque()

        for i in range(n):
            if not visited[i]:
                ans += 1
            
                visited[i] = True
                q.append(i)

                while q:
                    node = q.popleft()
                    for neigh in graph[node]:
                        if visited[neigh]:
                            continue
                        visited[neigh] = True
                        q.append(neigh)
        
        return ans
