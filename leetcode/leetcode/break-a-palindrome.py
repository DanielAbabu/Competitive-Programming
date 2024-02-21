class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        if len(palindrome) < 2:
            return ""

        if set(palindrome) == {'a'} or (len(palindrome) % 2 != 0 and len(set(palindrome)) == 2 and set(palindrome[:len(palindrome)//2]) == {'a'} and set(palindrome[len(palindrome)//2+1:]) == {'a'}):
            palindrome[-1] = "b"
            return "".join(palindrome)
        
        for i in range(len(palindrome)):
            if palindrome[i] != "a" :
                palindrome[i] = "a"
                break

        return "".join(palindrome)