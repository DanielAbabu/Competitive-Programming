class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller=[]
        equal=[]
        greater=[]
        for num in nums:
            if num>pivot:
                greater.append(num)
            elif num < pivot:
                smaller.append(num)
            else:
                equal.append(num)
        equal.extend(greater)
        smaller.extend(equal)
        return smaller