class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0
        for i in range(len(bank)):
           bank[i] = sum( map(int,list(bank[i])))

        tem=0
        for i in range(len(bank)):
            if bank[i] != 0:
                print(tem, bank[i])
                ans += tem*bank[i]
                tem = bank[i]
                

        return ans