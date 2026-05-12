# we can sort both strings and then perform a character comparison - TC: O(nlogn), SC: O(n)
# we can create a hashmap for both strings and then compare each pair - TC: O(n), SC: O(2n)
# we can create 2 lists (len - 26) and then increment corresponding index - TC: O(n), SC: O(2n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        
        return True