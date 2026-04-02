# keep track of the incoming and outgoing edges for each person
# the town judge node will have 0 outgoing edges and n-1 incoming edges
# create 2 arrays, one for incoming and one for outgoing
# Iterate through the trust list, update counts, 
# then check for a node with 0 outgoing and n-1 incoming edges

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = [0] * n
        outgoing = [0] * n

        for a, b in trust:
            outgoing[a-1] += 1
            incoming[b-1] += 1
        
        for i in range(n):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i + 1
        
        return -1