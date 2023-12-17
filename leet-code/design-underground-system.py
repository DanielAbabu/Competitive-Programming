class UndergroundSystem:

    def __init__(self):
        self.chin = defaultdict(list)
        self.tstart = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.chin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = (self.chin[id][0], stationName)
        dtime = t - self.chin[id][1]
        self.tstart[start].append(dtime)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        start = (startStation, endStation)
        
        time = self.tstart[start]
        return sum(time)/len(time)
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)