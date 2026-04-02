# we can use recursion to find the matches
# we can either choose to use the char or skip over the char
# TC: O(n * 2^n + m * k)
# we can improve on TC by using memoization, avoid calculating the same i
# TC: O(n^2 + m*k)

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i + 1)
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    res = min(res, dfs(j + 1))
                    
            dp[i] = res
            return res
        
        words = set(dictionary)
        dp = {len(s): 0}
        return dfs(0)