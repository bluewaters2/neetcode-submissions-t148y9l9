# we can iterate through the s and consider each character to be the center
# we expand to the left and right till the chars match
# maintain the startIdx and resLen to figure out the result string
# we tackle the even and odd case separately
# TC: O(n^2), SC: O(n)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen, startIdx = 0, 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    resLen = r - l + 1
                    startIdx = l
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    resLen = r - l + 1
                    startIdx = l
                l -= 1
                r += 1
        
        return s[startIdx:startIdx+resLen]