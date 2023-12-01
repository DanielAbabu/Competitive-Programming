class Solution:
    def interpret(self, command: str) -> str:
        i=0
        ans=""
        while i < len(command):
            if command[i] == "G":
                ans+= "G"
            elif command[i:i+2] == "()" :
                ans+= "o"
                i+=1
            elif command[i:i+4] == "(al)":
                ans+= "al"
                i+=3
            i+=1
        return ans

