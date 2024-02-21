class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        j = i = c = 0

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                c += 1
                i += 1
            j += 1
        
        return c
            
