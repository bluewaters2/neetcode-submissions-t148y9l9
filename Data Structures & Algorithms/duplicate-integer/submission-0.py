# we can sort nums, check whether duplicates are present, TC: O(nlogn), SC: O(1)
# we can use set to check for duplicates, TC: O(n), SC: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            if num in s:
                return True
            s.add(num)
        
        return False