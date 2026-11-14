class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # FACTS: the length of the result will be less than or equal to intervals. The array is not sorted 
        # For an O(nlogn) sol. we can sort the array now overlapping starts can be merged, This is the same question as insert interval except we are searching for the interval to insert.
        intervals.sort()
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                # Because it is sorted we know that the value for res start is either the exact same or less than interval[i][0] so we only need to change the end
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res 
           
          


            