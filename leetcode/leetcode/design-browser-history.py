class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.now = Node(homepage)
        
    def visit(self, url: str) -> None:
        curr = Node(url)
        self.now.next = curr
        curr.prev = self.now
        self.now = curr
        
    def back(self, steps: int) -> str:
        while steps and self.now.prev:
            self.now = self.now.prev
            steps -= 1

        return self.now.val
        

    def forward(self, steps: int) -> str:

        while steps and self.now.next:
            self.now = self.now.next
            steps -= 1
            
        return self.now.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)