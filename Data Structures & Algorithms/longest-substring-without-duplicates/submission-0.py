# we use two pointers to keep track of the window, we use a hashmap to store the (char, index)
# when we come across a char already in mp we calculate the window and modify the hashmap value
# we also calculate the maxLen at the end because the end char may not be in mp
# since we iterate through s once, TC: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxLen = 0, -1, 0
        mp = {}

        for r, char in enumerate(s):
            if char in mp:
                if maxLen < (r - l):
                    maxLen = r - l
                l = max(l, mp[char] + 1)
                
            mp[char] = r
        
        if maxLen < (r - l + 1):
            maxLen = r - l + 1
        
        return maxLen