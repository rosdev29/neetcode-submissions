import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)  # userId -> list of (time, tweetId)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []

        users = self.following[userId].copy()
        users.add(userId)

        for u in users:
            for time, tweetId in self.tweets[u][-10:]:
                heapq.heappush(heap, (time, tweetId))
                if len(heap) > 10:
                    heapq.heappop(heap)

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)