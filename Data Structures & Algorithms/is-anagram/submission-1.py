# we can sort both strings and then perform a character comparison - TC: O(nlogn), SC: O(n)
# we can create a hashmap for both strings and then compare each pair - TC: O(n), SC: O(2n)
# we can create 2 lists (len - 26) and then increment corresponding index - TC: O(n), SC: O(2n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def char_count(word, l):
            for char in word:
                idx = ord(char) - ord('a')
                l[idx-1] += 1

            return


        l1, l2 = [0] * 26, [0] * 26
        char_count(s, l1)
        char_count(t, l2)

        for i in range(26):
            if l1[i] != l2[i]:
                return False
        
        return True
        