class ATM:

    def __init__(self):
        self.atm = {500:0,200:0,100:0,50:0,20:0}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, notes in enumerate(self.atm):
            self.atm[notes] += banknotesCount[5-i-1]

    def withdraw(self, amount: int) -> List[int]:
        withdraw = [0] * 5
        for i, notes in enumerate(self.atm):
            t = min(self.atm[notes], amount // notes)
            amount -= t * notes
            withdraw[5-i-1] = t     
        if amount: return [-1]
        for i, notes in enumerate(self.atm):
            self.atm[notes] -= withdraw[5-i-1]
        return withdraw
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)