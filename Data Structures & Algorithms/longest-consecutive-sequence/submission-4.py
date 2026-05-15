# create a set to reduce lookup to O(1), we iterate through the array and then 
# check whether the consecutive numbers are present in set
# TC: O(n^2), SC: O(n)
# we can improve on this by making sure that num-1 is not in set
# then we make sure that we are at the beginning of a sequence
# TC: O(n), SC: O(n)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0

        for num in seen:
            if (num - 1) not in seen:
                length = 1
                while (num + length) in seen:
                    length += 1
                ans = max(ans, length)
        
        return ans