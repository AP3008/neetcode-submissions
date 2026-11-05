class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Taking the length our tracker to increment and result list 
        n = len(intervals)
        i = 0
        res = []

        # we loop through the array while the end of the ith interval is less than the new interval adding all of the intervals to our list 
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1 
        
        # If the end point of the new interval is greater or equal to the beginning of the next interval we want to create a new larger interval by taking the min of the start and the max of the ends, and we increment checking if the same can be done with the following interval as long as we are still in the list. 
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1 
        # After this we can add out new interval 
        res.append(newInterval)
        # if there are values leftover, we need to add them to the list 
        while i < n:
            res.append(intervals[i])
            i+=1 
        # Now we can return res 
        return res 