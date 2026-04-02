# we can use 2 pointer method to find whether the string is a palindrome after removal of 1 char
# since there is only 1 char at that point of mismatch we can check whether it's a palindrome after shifting one space

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return palindrome(l+1, r) or palindrome(l, r-1)
                
            l += 1
            r -= 1
        return True