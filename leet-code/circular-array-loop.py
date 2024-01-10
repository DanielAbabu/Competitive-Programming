class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            fast, slow = i, i
            count = n   
            j=0
            while j<n:
                fast = (fast + nums[fast]) % n
                if nums[fast] * nums[i] < 0:
                    break
                fast = (fast + nums[fast]) % n
                if nums[fast] * nums[i] < 0:
                    break

                slow = (slow + nums[slow]) % n
                next_slow = (slow + nums[slow]) % n
                if fast == slow and slow != next_slow:
                    return True
                j += 1
        
        return False


        

