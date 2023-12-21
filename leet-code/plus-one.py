class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        for digit in range(len(digits)):
            if digits[digit] != 9:
                
                digits[digit]+=1
                break
            if digit == len(digits)-1:
                digits.append(1)

            digits[digit]=0
        return reversed(digits)
        