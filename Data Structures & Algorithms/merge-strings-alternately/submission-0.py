class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        l1, l2 = len(word1), len(word2)

        i = 0
        while i < min(l1, l2):
            ans += word1[i]
            ans += word2[i]
            i += 1
        
        if i < l1:
            ans += word1[i:]
        
        if i < l2:
            ans += word2[i:]
        
        return ans