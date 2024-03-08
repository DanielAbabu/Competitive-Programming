
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.data[key].append( [value, timestamp] )

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.data:
            return res

        values = self.data[key]

        low, high = 0, len(values) - 1
        while low <= high:
            mid = (low + high) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                low = mid + 1
            else:
                 high = mid - 1

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)