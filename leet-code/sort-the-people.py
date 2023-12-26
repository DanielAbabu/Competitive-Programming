class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic=dict(zip(heights,names))
        flag=True
        for i in range(len(heights)):
            if flag:
                flag=False
                for j in range(len(heights)-1):
                    if heights[j]< heights[j+1]:
                        heights[j], heights[j+1] =  heights[j+1], heights[j]
                        flag=True
            else:
                break
        ans=[]
        for i in heights:
            ans.append(dic[i])

        return ans


        