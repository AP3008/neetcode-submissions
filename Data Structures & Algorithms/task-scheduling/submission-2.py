class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task takes 1 unit of time 
        
        # we take a counter for each task
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0)+1 
        # we take the values and make them negative to turn them into a maxHeap 
        maxHeap = [-x for x in count.values()]
        # Use heapify on the list of values, so the most frequent comes first 
        heapq.heapify(maxHeap)
        # Our result, keeping track of the time
        time = 0
        # a queue that keeps track of when we can place values again. 
        q = deque() # contains pairs of [-count, idleTime]
        # While either the q or the maxHeap has values we iterate. 
        while maxHeap or q:
            # increment the time by 1 
            time+=1 
            # If the maxHeap is not empty 
            if maxHeap:
                # we take the most frequent value and increment it by 1 because the value is negative, but this is essentially decrementing the counter, as it approaches 0.
                cnt = 1 + heapq.heappop(maxHeap)
                # If the cnt we just got is not zero we want to append it to the end of the queue, so we can handle it 
                if cnt:
                    # The time will be the current time + the idle time we have to wait 
                    q.append([cnt, time + n])
            # If the queue is not empty and the time is equal to the timer on that element of the queue, we want to add the element back to the heap as we have just ran it once through the CPU and need to schedule it's next task 
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        # Once the q and the heap are empty we can return the time. 
        return time 
