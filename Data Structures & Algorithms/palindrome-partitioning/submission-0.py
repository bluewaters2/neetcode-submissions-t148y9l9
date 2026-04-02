class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i):
            if i >= len(s):
                ans.append(curr.copy())
                return

            for j in range(i, len(s)):
                if self.palin(s, i, j):
                    curr.append(s[i:j+1])
                    dfs(j+1)
                    curr.pop()
            
        ans, curr = [], []    
        dfs(0)
        return ans
    
    def palin(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True