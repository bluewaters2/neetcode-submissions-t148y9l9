# we can use counter to group the words based on the sorted form of the word

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for word in strs:
            w = ''.join(sorted(word))
            if w not in mp:
                mp[w] = []

            mp[w].append(word)
        
        ans = []
        for val in mp.values():
            ans.append(val)
        
        return ans