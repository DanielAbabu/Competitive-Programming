class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []
        for log in logs:
            if stk and log == "../":
                stk.pop()
            elif log not in {"./","../"}:
                stk.append(log)

        return len(stk)