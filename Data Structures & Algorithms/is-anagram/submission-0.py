class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = Counter(s)

        for char in t:
            if char not in mp:
                return False
            mp[char] -= 1
            if mp[char] == 0:
                del mp[char]
        
        return len(mp) == 0