class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxLen = 0

        for num in nums:
            if num not in s:
                continue
            
            i = num

            while s and (num + 1) in s:
                s.remove(num + 1)
                num += 1
            
            while s and (i - 1) in s:
                s.remove(i - 1)
                i -= 1
            
            maxLen = max(maxLen, num - i + 1)
        
        return maxLen