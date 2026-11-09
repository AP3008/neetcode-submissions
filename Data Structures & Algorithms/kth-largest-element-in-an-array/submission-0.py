class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We can sort in O(nlog(n)) but we can heapify in O(n)
        # We need to use a max heap but values can be negative so, we can't use 
        nums = [-x for x in nums]
        heapq.heapify(nums)
        res = float('-inf')
        while k > 0:
            res = heapq.heappop(nums)
            k-=1
        return -res