# use 2 pointers and a hashmap to keep char: idx (key: value) pair
# TC: O(n), SC: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        mp = {}

        for right, char in enumerate(s):
            if char in mp and left < mp[char] + 1:
                left = mp[char] + 1
            
            mp[char] = right
            ans = max(ans, right - left + 1)
        
        return ans