class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left, odd, count, total = 0, 0, 0, 0

        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                odd += 1

                if odd >= k:
                    count = 1

                    while nums[left] % 2 == 0:
                        count += 1
                        left += 1

                    left += 1
                    total += count
            elif odd >= k:
                total += count

        return total