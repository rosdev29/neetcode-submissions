class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            prev_end = intervals[i - 1].end
            curr_start = intervals[i].start

            if curr_start < prev_end:
                return False

        return True