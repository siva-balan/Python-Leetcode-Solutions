class WordDictionary:

    # def __init__(self):
    #     self.child = {}
    #     self.iscomplete = False        

    # def addWord(self, word: str) -> None:
    #     curr =self
    #     for i in word:
    #         if i not in curr.child:
    #             curr.child[i] = WordDictionary()
    #         curr = curr.child[i]
    #     curr.iscomplete = True

    # def search(self, word: str) -> bool:
    #     curr = self

    #     for i in range(len(word)):
    #         if word[i] == ".":
    #             for ch in curr.child:
    #                 if ch != None and search(ch,word[i+1:]): return True
    #             return False
            
    #         if word[i] not in curr.child : return False
    #         curr = curr.child[word[i]]
        
    #     return curr != None and curr.iscomplete

    def __init__(self):
        self.children = [None]*26
        self.isCompleteWord = False
        

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = WordDictionary()
            curr = curr.children[ord(c) - ord('a')]
        
        curr.isCompleteWord = True
        

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch != None and ch.search(word[i+1:]): return True
                return False
            
            if curr.children[ord(c) - ord('a')] == None: return False
            curr = curr.children[ord(c) - ord('a')]
        
        return curr != None and curr.isCompleteWord

        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
