# use 2 pointers, calculate the area and shift the pointer with lower height
# TC: O(n) 

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        ans = 0

        while left < right:
            ans = max(ans, (min(heights[left], heights[right]) * (right - left)))
            
            if heights[left] > heights[right]:
                right -= 1
            
            else:
                left += 1
        
        return ans