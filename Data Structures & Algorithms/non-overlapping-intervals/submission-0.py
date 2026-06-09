class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[0])

        remove = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                remove += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end

        return remove