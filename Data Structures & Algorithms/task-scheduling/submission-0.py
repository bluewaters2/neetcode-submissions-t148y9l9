class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = {}
        for task in tasks:
            if task not in mp:
                mp[task] = 0
            mp[task] += 1
        
        heap = []
        for val, cnt in mp.items():
            heapq.heappush(heap, (-1 * cnt, val))
        
        ans = 0

        while heap:
            s = []
            for _ in range(n+1):
                if not heap and not s:
                    return ans
                
                if heap:
                    cnt, val = heapq.heappop(heap)
                    cnt += 1

                    if cnt < 0:
                        s.append((cnt, val))
            
                ans += 1
            
            for cnt, val in s:
                heapq.heappush(heap, (cnt, val))
        
        return ans