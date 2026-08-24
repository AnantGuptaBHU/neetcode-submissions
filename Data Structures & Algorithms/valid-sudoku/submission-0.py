class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in rows[i]:
                    return False
                if board[i][j] != '.' and board[i][j] in column[j]:
                    return False
                b = (i // 3) * 3 + (j // 3)
                if board[i][j] != '.' and board[i][j] in box[b]:
                    return False
                rows[i].add(board[i][j])
                column[j].add(board[i][j])
                box[b].add(board[i][j])
        return True
        