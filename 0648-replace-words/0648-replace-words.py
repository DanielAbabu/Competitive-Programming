class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for a in word:
            c = ord(a) - ord("a")

            if cur.children[c] == None:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.is_end = True           
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        ans = []

        for a in prefix:
            c = ord(a) - ord("a")
            if cur.children[c] == None:
                return ""

            ans.append(a)
            cur = cur.children[c]
            if cur.is_end:
                return "".join(ans)



        return ""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(" ")

        trie = Trie()
        for a in dictionary:
            trie.insert(a)

        ans = []
        for a in sentence:
            tem = trie.startsWith(a)
            if tem:
                ans.append(tem)
            else:
                ans.append(a)

        return " ".join(ans)


        

        