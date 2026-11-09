class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # We want to calculate all of the distances and keep track of the points that go us there. O(n) operation 
        minHeap = []
        for x, y in points:
            # We don't take the square root because we know that if this is larger then the square root will still be larger 
            dist = (x**2) + (y**2)
            # we append the distance and coordinates to our list
            minHeap.append([dist,x,y])
        # We make our list a minHeap (O(n) operation NOT O(nlog(n)))
        heapq.heapify(minHeap)
        # We have our resulting list 
        res = []
        # while k is not 0 we want to pop our minheap since it organizes based of the first element in the list, so the smallest distance will be first. 
        while k > 0:
            # We just pop the smallest element of the heap and append it to res, and decrement k.
            dis, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        # Once k is 0, res will be populated with coordinates. 
        return res 