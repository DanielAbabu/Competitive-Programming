class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def win( l, r):
            if l == r:
                return nums[l]

            left = nums[l] - win(l+1, r)
            right = nums[r] - win(l, r -1 )

            return max(left , right)


        return  win( 0, len(nums)-1) >= 0             

