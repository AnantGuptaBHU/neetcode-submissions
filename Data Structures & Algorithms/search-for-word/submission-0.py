class Solution:
    def fun(self, board, i, j, s, word,m,n):
        if s == word:
            return True
        a = len(s)
        c = word[a]
        if i < 0 or i >= m or j < 0 or j >= n or c != board[i][j]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        found = (self.fun(board, i+1, j, s+temp, word,m,n) or self.fun(board, i, j+1, s+temp, word,m,n) or self.fun(board, i-1, j, s+temp, word,m,n) or self.fun(board, i, j-1, s+temp, word,m,n))
        board[i][j] = temp
        return found
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.fun(board, i, j, '', word, m, n):
                    return True
        return False