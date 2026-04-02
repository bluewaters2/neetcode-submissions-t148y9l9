# we can sort the array and compare the first and last word in the array to find the longest common prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]

        for i, char in enumerate(first):
            if char != last[i]:
                return first[:i]
        
        return first