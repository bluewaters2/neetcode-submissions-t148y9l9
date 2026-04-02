class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans, maxcnt = 0, 0
        mp = Counter()

        for right, char in enumerate(s):
            mp[char] += 1
            maxcnt = max(maxcnt, mp[char])

            while right - left + 1 > k + maxcnt:
                mp[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
        