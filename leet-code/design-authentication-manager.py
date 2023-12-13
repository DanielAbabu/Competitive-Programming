class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.dic = defaultdict()
        self.timeToLive = timeToLive
  
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dic[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.dic and self.dic[tokenId] + self.timeToLive > currentTime:
            self.dic[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        c = 0
        for token, expiration_time in self.dic.items():
            if expiration_time + self.timeToLive > currentTime:
                c += 1
        return c


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)