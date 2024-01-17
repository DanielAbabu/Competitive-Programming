class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxm = left = 0
        dic = defaultdict(int)

        for i in range(len(fruits)):
            dic[fruits[i]] += 1

            while len(dic)>2:
                dic[fruits[left]] -= 1
                if dic[fruits[left]] == 0:
                    del dic[fruits[left]]
                left+=1

            maxm = max(maxm, i-left+1)

        return maxm


