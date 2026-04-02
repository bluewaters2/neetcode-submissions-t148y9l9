class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = []
        self.k = k

        for num in nums:
            heapq.heappush(self.queue, num)
        
        while len(self.queue) > k:
            heapq.heappop(self.queue)

    def add(self, val: int) -> int:
        if len(self.queue) < self.k:
            heapq.heappush(self.queue, val)
            return self.queue[0]
        
        min_val = heapq.heappop(self.queue)
        if min_val > val:
            heapq.heappush(self.queue, min_val)
        else:
            heapq.heappush(self.queue, val)
        
        return self.queue[0]