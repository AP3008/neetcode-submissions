"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # IDEA: We keep track of the largest end time we have seen and earliest start time not belonging to the same end time. This doesn't make sense
        # NAIVE: sort the list, compare the end time of the first to the begin time of the second and make sure it doesn't overlap. 

        for i in range(len(intervals)):
            for j in range(len(intervals)-i-1):
                if intervals[j].start > intervals[j+1].start:
                    intervals[j], intervals[j+1] = intervals[j+1], intervals[j]

        for i in range(len(intervals)-1):
            if intervals[i+1].start < intervals[i].end:
                return False 
        return True 
