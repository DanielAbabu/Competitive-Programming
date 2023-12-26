class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr= Counter(arr1)
        arr1=set(arr1)
        ans=[]

        for i in arr2:
            if i in arr1:
                ans+=[i]*arr[i]
                arr1.remove(i)
        
        arr1=sorted(list(arr1))
        for i in arr1:
            ans+=[i]*arr[i]

        return ans
            
            

        