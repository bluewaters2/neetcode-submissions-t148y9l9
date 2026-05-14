# create a set to reduce lookup to O(1), we iterate through the array and then check whether the consecutive numbers are present in set
# TC: O(n^2), SC: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0

        for num in nums:
            j, cnt = num, 0
            while j in seen:
                cnt += 1
                j += 1

            ans = max(ans, cnt)
        
        return ans