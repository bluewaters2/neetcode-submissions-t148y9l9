class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mp = {5: 0, 10: 0}

        for b in bills:
            if b == 5:
                mp[5] += 1
            
            elif b == 10:
                if mp[5] < 1:
                    return False
                else:
                    mp[5] -= 1
                    mp[10] += 1
            
            else:
                if (mp[10] >= 1 and mp[5] >= 1) or mp[5] >= 3:
                    if mp[10] >= 1:
                        mp[10] -= 1
                    
                    else:
                        mp[5] -= 2
                    
                    mp[5] -= 1
                
                else:
                    return False
        
        return True