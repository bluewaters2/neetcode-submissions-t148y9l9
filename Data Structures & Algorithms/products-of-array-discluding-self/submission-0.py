# we can solve the problem in TC: O(n)
# create an ans array, then we find the product of all elements before it and then all elements after it
# ans[i] = pref[i] * suff[i]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [nums[0]] * len(nums)

        for i in range(1, len(nums)-1):
            ans[i] = ans[i-1] * nums[i]
        
        p = 1
        for i in range(len(nums)-1, 0, -1):
            ans[i] = p * ans[i-1]
            p *= nums[i]
        
        ans[0] = p
        return ans