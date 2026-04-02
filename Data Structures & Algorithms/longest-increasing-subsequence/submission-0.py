# we can use 2 for loops to find the longest subsequence
# TC is O(n^2) and we can improve TC by using dp + binary search
# we create an array and if the ith value is more than the last entry in array we just append
# else we use bisect_left to find the index the value should be present
# TC: O(nlogn)
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            
            else:
                idx = bisect.bisect_left(dp, nums[i])
                dp[idx] = nums[i]
        
        return len(dp)