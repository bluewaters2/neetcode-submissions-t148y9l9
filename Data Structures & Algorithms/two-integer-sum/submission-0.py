class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, num in enumerate(nums):
            b = target - num
            if b in mp and mp[b] != i:
                return [i, mp[b]] if i < mp[b] else [mp[b], i]
            mp[num] = i
        
        return []