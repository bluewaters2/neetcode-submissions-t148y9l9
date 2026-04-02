# impossible arrangement is when count of any char is more than (n+1)//2 
# we can rearrange based on the count of chars using heap
# TC: O(nlogk) where k = 26

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        mp = Counter(s)

        heap, ans = [], []

        for key, val in mp.items():
            if val > (n + 1) // 2:
                return ''
            heapq.heappush(heap, (-1 * val, key))
        
        prev = None
        while heap:
            v, c = heapq.heappop(heap)
            if prev is not None and prev == c:
                v1, c1 = heapq.heappop(heap)
                ans.append(c1)
                prev = c1
                if v1 + 1 < 0:
                    heapq.heappush(heap, (v1 + 1, c1))
                
            else:
                v += 1
                prev = c
                ans.append(c)
            
            if v < 0:
                heapq.heappush(heap, (v, c))
        
        return ''.join(ans)