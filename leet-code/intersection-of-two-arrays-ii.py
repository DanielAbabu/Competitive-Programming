class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num=Counter(nums1)
        ans=[]

        for i in nums2:
            if num[i]:
                ans.append(i)
                num[i]-=1
        
        return ans

        