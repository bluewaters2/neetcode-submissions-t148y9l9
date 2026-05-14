class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [1] * l

        for i in range(1, l):
            ans[i] = ans[i-1] * nums[i-1]
        print(ans)
        
        p = nums[-1]
        for i in range(l-2, -1, -1):
            ans[i] *= p
            p *= nums[i]
        
        return ans