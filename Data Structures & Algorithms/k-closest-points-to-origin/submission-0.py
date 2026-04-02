class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for i, point in enumerate(points):
            a, b = point
            dist = (a * a) + (b * b)
            heapq.heappush(h, (dist, i))
        
        ans = []

        while k:
            d, i = heapq.heappop(h)
            ans.append(points[i])
            k -= 1
        
        return ans