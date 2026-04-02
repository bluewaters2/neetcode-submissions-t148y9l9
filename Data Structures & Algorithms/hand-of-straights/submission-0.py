class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        mp = Counter(hand)
        hand.sort()

        for h in hand:
            if h not in mp:
                continue
            
            cnt = 0
            while mp and h in mp and cnt != groupSize:
                mp[h] -= 1
                if mp[h] == 0:
                    del mp[h]
                
                cnt += 1
                h += 1
            
            if cnt != groupSize:
                return False
        
        return True