# initialize 2 min-heaps, one to store (enqueue_time, (processingTime, index))


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        enqueue_min_heap = []
        processing_min_heap = []

        ans, time = [], 0

        for i, task in enumerate(tasks):
            enqueue_time, process_time = task
            heapq.heappush(enqueue_min_heap, (enqueue_time, process_time, i))
        
        while enqueue_min_heap or processing_min_heap:
            while enqueue_min_heap and enqueue_min_heap[0][0] <= time:
                enqueue_time, process_time, i = heapq.heappop(enqueue_min_heap)
                heapq.heappush(processing_min_heap, (process_time, i))
            
            if not processing_min_heap:
                time = enqueue_min_heap[0][0]
                continue
            
            process_time, i = heapq.heappop(processing_min_heap)
            time += process_time
            ans.append(i)
        
        return ans