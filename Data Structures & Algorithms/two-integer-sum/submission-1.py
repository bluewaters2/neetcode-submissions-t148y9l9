# to find the pair (i, j) we can use 2 for loops to find the (nums[i], nums[j]) - TC: O(n^2), SC: O(1)
# we can reduce the TC by using 1 for loop and hashmap, hashmap will store the indices and then use for lookup - TC: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = {}
        
        for i, num in enumerate(nums):
            if (target - num) in cnt and cnt[target - num] != i:
                return [cnt[target - num], i]
            cnt[num] = i
        
        return [-1, -1]
            