# we can sort the intervals list and then compare two intervals to find overlapping

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = [intervals[0]]
        i = 1

        while i < len(intervals):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][0] = min(ans[-1][0], intervals[i][0])
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            
            else:
                ans.append(intervals[i])
            
            i += 1
        
        return ans