class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        result = []

        for i in range(max_len):
            temp = ""
            for word in words:
                if len(word) > i:
                    temp += word[i]
                else:
                    temp += " "
            result.append(temp.rstrip())

        return result
