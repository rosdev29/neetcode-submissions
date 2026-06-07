import heapq

class MedianFinder:

    def __init__(self):
        self.left = []   # max heap
        self.right = []  # min heap

    def addNum(self, num: int) -> None:

        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        # rebalance
        if len(self.left) > len(self.right) + 1:
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)

        elif len(self.right) > len(self.left) + 1:
            x = heapq.heappop(self.right)
            heapq.heappush(self.left, -x)

    def findMedian(self) -> float:

        if len(self.left) > len(self.right):
            return -self.left[0]

        if len(self.right) > len(self.left):
            return self.right[0]

        return (-self.left[0] + self.right[0]) / 2