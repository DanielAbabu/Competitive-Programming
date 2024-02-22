class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        monostk = []
        for i in range(len(nums2)):
            while monostk and nums2[ monostk[-1] ] < nums2[i]:
                d[ nums2[ monostk[-1] ] ] = nums2[i]
                monostk.pop()
            
            monostk.append(i)

        ans = []
        for i in nums1:
            ans.append( d.get(i,-1) )
              
        return ans