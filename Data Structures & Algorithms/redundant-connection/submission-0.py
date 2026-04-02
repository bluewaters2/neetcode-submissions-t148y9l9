# we can use dfs to find whether a cycle is present in the graph
# we iterate through the edges and perform dfs on each edge

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, parent):
            # a cycle found
            if visit[node]:
                return True

            # we change the value of corresponding node that we visit
            visit[node] = True
            # we iterate through each neighbour of a node
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                # we check for the new neighbour
                if dfs(neigh, node):
                    return True
            
            return False
        
        # we start from the first edge and perform dfs as we progress through the graph
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = [False] * (n + 1)
        
            if dfs(u, -1):
                return [u, v]
        
        return []