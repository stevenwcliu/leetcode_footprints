from collections import defaultdict
class Leaderboard:

    def __init__(self):
        # scoreboard = defaultdict()
        self.scores = defaultdict() # correction
        
        
    def addScore(self, playerId: int, score: int) -> None:
        # if not self.scoreboard[playerId]:
        if playerId not in self.scores: # correction
            self.scores[playerId] = 0
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        # how to find the top k score from the scoreboard quickly?
        # heap?
        heap = []
        for x in self.scores.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res
        
    def reset(self, playerId: int) -> None:
        # if self.scoreboard[playerId]: # playerId guranteed to be in the leadershipBoard
        self.scores[playerId] = 0
        
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)