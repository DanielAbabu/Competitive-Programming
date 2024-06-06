class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c= Counter(hand)
        check = sorted(list(set(hand)))

        for i in range(len(check)):
            while c[check[i]] > 0:
                tem = check[i]-1
                for j in range(i,i+groupSize):
                    if  j >= len(check) or tem+1 != check[j] or c[check[j]] <= 0:
                        return False
                    c[check[j]] -= 1
                    tem = check[j]
        return True         
