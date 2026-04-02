# since the problem is calculating the min time it takes for all of the n nodes to receive signal
# it's a weighed directed graph, so we use dijkstra's algorithm to find the min time
import math
inf = math.inf

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_time = [inf] * (n + 1)
        min_time[0] = min_time[k] = 0

        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        q = [(0, k)]

        while q:
            t, node = heapq.heappop(q)
            for neigh, t1 in graph[node]:
                new_time = t1 + t
                if min_time[neigh] > new_time:
                    min_time[neigh] = new_time
                    heapq.heappush(q, (new_time, neigh))
        
        ans = max(min_time)
        return ans if ans != inf else -1