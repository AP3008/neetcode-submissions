class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: # This is because the values are negative, so second is the smaller stone 
                heapq.heappush(stones, first - second)
        return abs(stones[0]) if stones else 0 
