class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f=set("qwertyuiop")
        s=set("asdfghjkl")
        t=set("zxcvbnm")
        ans=[]

        for wor in words:
          tem=wor
          word=set(wor.lower())
          print(word)
          if word.issubset(f) or word.issubset(s) or  word.issubset(t) :
            ans.append(tem)

        return ans