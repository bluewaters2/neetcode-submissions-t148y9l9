# we have to check whether all the nodes are connected
# also check that there are no cycles present in the graph
# we 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node, parent):
            if visited[node] or node == parent:
                return False
            visited[node] = True
            for next_node in graph[node]:
                if next_node != parent:
                    if not dfs(next_node, node):
                        return False
            return True


        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        if not dfs(0, -1):
            return False

        return all(visited)