class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hor = collections.defaultdict(set)
        ver = collections.defaultdict(set)
        box = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
            
                if board[i][j] == '.':
                    continue
                
                if (board[i][j] in hor[i] or board[i][j] in ver[j] or board[i][j] in box[(i//3,j//3)]):
                    return False
                hor[i].add(board[i][j])
                ver[j].add(board[i][j])
                box[(i//3,j//3)].add(board[i][j])
        return True
