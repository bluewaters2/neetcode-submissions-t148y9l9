class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False
        i = 0

        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i]) 
            
            elif intervals[i][0] > newInterval[1]:
                if inserted == False:
                    res.append(newInterval)
                    inserted = True
                res.append(intervals[i])
            
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
            i += 1
        
        if inserted == False:
            res.append(newInterval)
        
        return res