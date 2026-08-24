class Solution:
    def is_valid(self, board, row, col, n):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
    def backtrack(self, board, res, n, curr_row):
        if curr_row >=n:
            res.append([''.join(row) for row in board])
            return
        for i in range(n):
            if self.is_valid(board, curr_row, i, n):
                board[curr_row][i] = 'Q'
                self.backtrack(board, res, n, curr_row+1)
                board[curr_row][i] = '.'

    def solveNQueens(self, n):
        res = []
        board = [['.' for i in range(n)] for _ in range(n)]
        self.backtrack(board, res, n, 0)
        return res
        