class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)
        locate = {}

        for i, r in enumerate(list1):
            if r in common:
                locate[r] = i 

        for i, r in enumerate(list2):
            if r in common:
                locate[r] += i 

        minm = min(locate.values())

        return [key for key, value in locate.items() if value == minm]