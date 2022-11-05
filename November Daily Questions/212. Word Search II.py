
# cOMMENTED CODE IS CORRECT BUT TIME LIMIT EXCEDDED. THE NEXT IS TAKAN FROM LEETCODE DISCUSS SECTION

"""class TrieNode:
    def __init__(self):
        self.children ={}
        self.isWord =False

    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for w in words:
            root.addWord(w)

        m = len(board)
        n = len(board[0])
        output = set()
        visit = set()

        def dfs(r,c,node,word):
            if (r<0 or c<0 or r==m or c==n or board[r][c] not in node.children or (r,c) in visit):
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                output.add(word)
            
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))

        for r in range(m):
            for c in range(n):
                dfs(r,c,root,"")
        
        return list(output)"""


from functools import reduce
from collections import defaultdict

def prune(trie, word):
    t = trie
    nodes = []
    for c in word:
        if c not in t:
            return False
        t = t[c]
        nodes.append((t, c))
    if "#" in t:
        p = "#"
        for node, c in nodes[::-1]:
            if len(node[p]) == 0 or p == "#":
                del node[p]
            p = c

class Solution:
    def findWords(self, board: List[List[str]], words: List[str])-> List[str]:
        COLS, ROWS = len(board), len(board[0])
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = "#"
        
        for word in words:
            reduce(dict.__getitem__, word, trie)[END] = word

        def adj(x, y):
            for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if 0 <= x+i < COLS and 0 <= y+j < ROWS:
                    yield (x+i, y+j)

        ans = set()
        def DFS(i, j, node):
            if END in node:
                ans.add(node[END]) # stored the word in the terminal nodes
                prune(trie, node[END]) # prune the found word for avoiding later duplicates

            letter = board[i][j] # keep for later restoration
            board[i][j] = "" # mark as visited
            for x, y in adj(i,j):
                if board[x][y] in node:
                    DFS(x, y, node[board[x][y]])
            board[i][j] = letter # restore board
            return

        for i in range(COLS):
            for j in range(ROWS):
                if board[i][j] in trie:
                    DFS(i, j, trie[board[i][j]])
        return ans
