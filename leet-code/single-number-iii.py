class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for a in nums:
            xor ^= a

        mask = xor & -xor

        a = b = 0
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num

        

        return [a,b]