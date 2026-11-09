class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # result list 
        res = []
        # left and right pointers started at the beginning of the list 
        l = r = 0
        # Our queue so we can popleft() in O(1), pop() O(1) and append in O(1)
        q = deque() 

        # We look until r is out of bounds 
        while r < len(nums):
            # If the top values of the queue is less than the current value, we know it can never be considered the greatest in the window, so we want to pop all of the smaller values out 
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # Once the smaller values have been popped out we can append r to our queue 
            q.append(r)

            # If the left index is greater than the index of the first element in our queue, that means that element is outisde of our window, so we need to remove it. 
            if l > q[0]:
                q.popleft()
            
            # If the next iteration results in us being outside of the window, we want to append the value at the beginning of the list to our result. 
            if (r+1) >= k:
                # Only in this case do we need to move the left pointer. So the window stays of size k.
                # The value at q[0] should always be the largest value in the window, since we popout all smaller values if we encounter a larger value. 
                res.append(nums[q[0]])
                l+=1
            # On every iteration we increment the right pointer. 
            r+=1
        return res 