class Solution:
    def minInterval(self, intervals, queries):
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        intervals.sort()

        res = [-1] * len(queries)
        heap = []
        j = 0

        for q, idx in sorted_queries:
            while j < len(intervals) and intervals[j][0] <= q:
                l, r = intervals[j]
                heapq.heappush(heap, (r - l + 1, r))
                j += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                res[idx] = heap[0][0]

        return res