#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.isWord = True

    def search(self, word: str) -> bool:

        def dfs(node,subword):
            curr = node
            if subword == "":
                return curr.isWord

            c = subword[0]
            if c == ".":
                for ch in curr.children:
                    if dfs(curr.children[ch],subword[1:]):
                        return True
                return False
            else:
                if c not in curr.children:
                    return False
                return dfs(curr.children[c],subword[1:])

        return dfs(self.root,word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

