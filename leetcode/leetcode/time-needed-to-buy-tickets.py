class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        x = tickets[k]
        tickets[k] = "x"
        i = ans = 0
        tickets = deque(tickets)

        while True:
            ans += 1
            if tickets[0] == "x":
                x -= 1
                if x == 0:
                    break
                tickets.append(tickets.popleft())

            elif tickets[0] - 1 != 0:
                tickets[0] -= 1
                tickets.append(tickets.popleft())
            else:
                tickets.popleft()

        return ans
