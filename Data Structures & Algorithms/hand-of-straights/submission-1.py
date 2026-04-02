class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        mp = Counter(hand)
        for h in hand:
            start = h
            while mp[start - 1]:
                start -= 1
            
            while start <= h:
                while mp[start]:
                    for i in range(start, start + groupSize):
                        if not mp[i]:
                            return False
                        mp[i] -= 1
                start += 1
        
        return True