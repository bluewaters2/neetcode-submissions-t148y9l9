# 2 pointers at both end and then shift to check whether palindrome
# string to lowercase, skip over the spaces
# TC: O(n), SC: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        s = s.lower()

        while left < right:
            while (left < right) and not (('a' <= s[left]  <= 'z') or ('0' <= s[left] <= '9')):
                left += 1

            while (left < right) and not (('a' <= s[right]  <= 'z') or ('0' <= s[right] <= '9')):
                right -= 1
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
            
