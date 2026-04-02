# we can use recursion to find the matches
# we can either choose to use the char or skip over the char
# TC: O(n * 2^n + m * k)
# we can improve on TC by using memoization, avoid calculating the same i
# TC: O(n^3 + m*k)
# we can further improve on TC by using a trie (prefix tree) to check the words
# TC: O(n^2 + m*k)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()

        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.end = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i + 1)
            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.end:
                    res = min(res, dfs(j + 1))

            dp[i] = res
            return res
        
        trie = Trie(dictionary)
        dp = {len(s): 0}
        return dfs(0)