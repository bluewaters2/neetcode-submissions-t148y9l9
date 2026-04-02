class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()

        while l < r:
            while l < len(s) and not ('a' <= s[l] and s[l] <= 'z') and not (s[l] >= '0' and s[l] <= '9'):
                l += 1

            while r > 0 and not ('a' <= s[r] and s[r] <= 'z') and not (s[r] >= '0' and s[r] <= '9'):
                r -= 1
            
            if l < r and s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True