# we can use 2 for loops to find whether duplicate exists - TC: O(n^2), SC: O(n)
# we can use a hashset or hashmap to check whether duplicate exists - TC: O(n), SC: O(n)
# 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False