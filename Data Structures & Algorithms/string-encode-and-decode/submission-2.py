# we encode each string with its length, a separator and then the string itself
# decode - read till separator '#' to get the length and then use indexing in string to get the string
# TC: O(m) for each decode() and encode() function calls
# SC: O(m+n) for each encode() and decode() function calls

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        ans = ''

        for word in strs:
            l = len(word)
            ans += str(l)
            ans += '#'
            ans += word

        return ans


    def decode(self, s: str) -> List[str]:

        if len(s) == 0:
            return []

        ans = []

        i = 0
        while i < len(s):
            l = ''
            while s[i] != '#':
                l += s[i]
                i += 1
            
            # get after the separator
            i += 1
            l = int(l)

            word = s[i:i+l]
            ans.append(word)
            i = i + l
        
        return ans



