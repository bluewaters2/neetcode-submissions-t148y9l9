# we can use a heap to keep track of the max element in each window
# TC: O(nlogn), store (value, index) pair

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-1 * num, i))

            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            
            if i - k >= -1:
                ans.append(-1 * heap[0][0])
        
        return ans