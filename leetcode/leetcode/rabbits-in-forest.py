class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c= Counter(answers)
        rabbit = 0
        for ans,rab in c.items():
            if ans+1 < rab and ans != 0:
                if rab%(ans+1) != 0:
                    rabbit += (ans+1) - rab%(ans+1)
            elif ans >= rab and ans != 0:
                rabbit +=  ans - rab +1


        return rabbit + len(answers)
