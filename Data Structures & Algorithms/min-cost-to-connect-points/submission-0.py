# we apply prim's algo to find the mst
# build adjacency list and adjacency matrix and store info about the nodes with the manhattan distance
# we start from an arbitary node and then we choose the node with the smallest cost
# TC: O(n^2 logn)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visit = set()
        q = [[0, 0]]
        while len(visit) < n:
            cost, i = heapq.heappop(q)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for nei_cost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(q, [nei_cost, nei])

        return res