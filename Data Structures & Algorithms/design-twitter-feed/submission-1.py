class Twitter:

    def __init__(self):
        self.cnt = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.cnt, tweetId])
        #decrement for max heap
        self.cnt -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # ordered starting from most recent
        min_heap = []

        # account for users own posts on their own feed 
        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if self.tweet_map[followeeId]:
                idx = len(self.tweet_map[followeeId]) - 1
                cnt, tweetID = self.tweet_map[followeeId][idx]
                min_heap.append([cnt, tweetID, followeeId, idx - 1])

        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            cnt, tweetID, followeeId, idx = heapq.heappop(min_heap)
            res.append(tweetID)
            if idx >= 0:
                cnt, tweetID = self.tweet_map[followeeId][idx]
                heapq.heappush(min_heap, [cnt, tweetID, followeeId, idx - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
