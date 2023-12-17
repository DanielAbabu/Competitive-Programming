class Bitset:
    def __init__(self, size: int):
        self.size= size
        self.bits ={"0": ["0"] * size, "1": ["1"] * size}
        self.currbit= "0"
        self.obit= 0

    def fix(self, idx: int) -> None:
        self.obit+= self.bits[self.currbit][idx] == "0"
        self.bits[self.currbit][idx]= "1"
        self.bits["1" if self.currbit=="0" else "0"][idx] = "0"

    def unfix(self, idx: int) -> None:
        self.obit-= self.bits[self.currbit][idx] == "1"
        self.bits[self.currbit][idx]= "0"
        self.bits["1" if self.currbit== "0" else "0"][idx] = "1"

    def flip(self) -> None:
        self.currbit = "1" if self.currbit== "0" else "0"
        self.obit= self.size -self.obit

    def all(self) -> bool:
        return self.obit== self.size

    def one(self) -> bool:
        return self.obit>0

    def count(self) -> int:
        return self.obit

    def toString(self) -> str:
        return "".join(self.bits[self.currbit])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()