class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0

        store = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        i = 0
        while i < len(s):
            if i < len(s)-1 and store[s[i]] < store[s[i+1]]:
                ans += (store[s[i+1]] - store[s[i]])
                i += 1
            
            else:
                ans += store[s[i]]

            i += 1
        
        return ans
