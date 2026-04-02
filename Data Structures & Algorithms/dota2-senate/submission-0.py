# multiple rounds can be made to find the victory
# maintain 2 queues, and store the indexes in separate queues
# compare and append the lower index back for next round

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        d_queue, r_queue = deque(), deque()

        for i, s in enumerate(senate):
            if s == 'R':
                r_queue.appendleft(i)
            else:
                d_queue.appendleft(i)
        
        while r_queue and d_queue:
            a, b = r_queue.pop(), d_queue.pop()
            if a > b:
                d_queue.appendleft(a + n)
            else:
                r_queue.appendleft(b + n)
        
        return "Radiant" if r_queue else "Dire"