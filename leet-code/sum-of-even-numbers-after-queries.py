class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        even = lambda x : not x%2
        tot = sum(filter(even,nums))

        for a , b in queries:
           
            tem = nums[b] + a
            if not nums[b] % 2 and not tem % 2 :
                tot += a
            elif not nums[b] % 2 and tem % 2:
                tot -= nums[b]
            elif nums[b] % 2 and not tem % 2:
                tot += tem
            nums[b] = tem
            ans.append(tot)
        return ans





5.