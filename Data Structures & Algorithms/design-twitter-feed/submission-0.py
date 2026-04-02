# we can store the postTweet with timestamp in priority queue so that most recent tweets are on top
# we can store the followers in a set to have a O(1) lookup
# and we can unfollow in O(1) TC too
# for getNewsFeed() pops elements from priority queue until len() > 0 or cnt != 10

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.store_tweets = []
        self.followers = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followers:
            self.followers[userId] = {userId}
        
        heapq.heappush(self.store_tweets, (-1 * self.timestamp, userId, tweetId))
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followers:
            return []
        ans = []
        store = []
        cnt = 0
        while self.store_tweets and cnt != 10:
            t, u, tid = heapq.heappop(self.store_tweets)
            if u == userId or u in self.followers[userId]:
                ans.append(tid)
                cnt += 1
            store.append((t, u, tid))
        
        for i in range(len(store)):
            heapq.heappush(self.store_tweets, store[i])
        
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = {followeeId}
        else:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

        
