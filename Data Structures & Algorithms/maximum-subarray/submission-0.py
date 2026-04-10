class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub, cur_sub = nums[0], nums[0]

        for i in range(1, len(nums)):
            if cur_sub + nums[i] > nums[i]:
                cur_sub += nums[i]
            else:
                cur_sub = nums[i]
            
            max_sub = max(max_sub, cur_sub)
        
        return max_sub