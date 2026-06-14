class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        
        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]
            print(i1.start, i1.end, "|", i2.start, i2.end)
            if i1.end > i2.start:
                return False
        return True
