# we find the frequency of each element and store in a hashmap
# sort the hashmap based on the mp.values() and then return the top k elements
# or we can use a priority queue to store the top 5 elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)

        pq = []
        for cnt, v in mp.items():
            heapq.heappush(pq, (v, cnt))
            if len(pq) > k:
                heapq.heappop(pq)

        ans = [k for v, k in pq]
        return ans