class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = Counter(list(words[0]))
        for i in range(1,len(words)):
            tem = Counter(list(words[i]))
            for a in ans:
                if ans[a] > tem[a]:
                    ans[a] = tem[a]


        pp = []
        for a in ans:
            if ans[a] >0 :
                pp.extend([a]*ans[a])
        return pp
        