# have a hashmap to store the anagrams
# iterate through the given list, sort the word, check whether sorted word is present in hashmap then add it to values

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for i, word in enumerate(strs):
            arranged_word = ''.join(sorted(word))
            if arranged_word in mp:
                mp[arranged_word].append(word)
            else:
                mp[arranged_word] = [word]
            
        ans = []
        for k, val in mp.items():
            ans.append(val)
        
        return ans