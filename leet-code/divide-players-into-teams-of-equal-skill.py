class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) - 1
        target = skill[l] + skill[r]
        ans = 0

        while l < r:
            currSum = skill[l] + skill[r]
            
            if currSum != target: return -1

            ans += skill[l] * skill[r]
            l += 1
            r -= 1

        return ans