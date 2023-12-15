class FrequencyTracker:

    def __init__(self):
        self.freq=defaultdict(int)
        self.ans=defaultdict(int)

    def add(self, number: int) -> None:
        if self.ans.get(self.freq[number]):
            self.ans[self.freq[number]]-=1

        self.freq[number] += 1
        self.ans[self.freq[number]] +=1
            
    def deleteOne(self, number: int) -> None:
        if self.freq[number]>0:
            self.ans[self.freq[number]]-=1
            self.freq[number]-= 1
            self.ans[self.freq[number]] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        if self.ans[frequency] >=1:
            return True

        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)