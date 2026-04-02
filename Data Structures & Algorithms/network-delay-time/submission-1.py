# since the problem is calculating the min time it takes for all of the n nodes to receive signal
# it's a weighed directed graph, so we use dijkstra's algorithm to find the min time
import math
inf = math.inf

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        q = [(0, k)]
        visited = set()

        t = 0
        while q:
            t, node = heapq.heappop(q)
            if node in visited:
                continue
            visited.add(node)
            ans = t
            for neigh, t1 in graph[node]:
                if neigh not in visited:
                    heapq.heappush(q, (t1+t, neigh))
        
        return ans if len(visited) == n else -1