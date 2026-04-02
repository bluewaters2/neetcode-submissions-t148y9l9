# we iterate through nums and if it matches the stored num then we increase the cnt
# else decrease, and if cnt < 0 then we change the stored num to a new num
# TC: O(n), SC: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val, cnt = nums[0], 0

        for num in nums:
            cnt += 1 if num == val else -1
            if cnt < 0:
                cnt = 1
                val = num
        
        return val