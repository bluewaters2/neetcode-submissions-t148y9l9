# we can also use a deque to keep the max values
# this is an improvement over heap as no need heapify, TC: O(n)
# we store the index of the elements
# since we can add and remove from both ends

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        ans = []
        q = deque()

        while r < len(nums):
            while q and nums[q[0]] < nums[r]:
                q.popleft()
            
            q.appendleft(r)
            
            if q[-1] < l:
                q.pop()
            
            if r - k >= -1:
                ans.append(nums[q[-1]])
                l += 1
            r += 1
        
        return ans