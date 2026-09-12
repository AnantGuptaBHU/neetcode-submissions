class Solution:
    def markRotten(self, grid, m, n):
        flag = False
        for i in range(0,m):
            for j in range(0,n):
                if (grid[i][j] == 1) and ((j>=1 and grid[i][j-1] == 2) or (j < n-1 and grid[i][j+1] == 2) or (i>=1 and grid[i-1][j] == 2) or (i < m-1 and grid[i+1][j] == 2)):
                    grid[i][j] = -2
                    flag = True
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -2:
                    grid[i][j] = 2
        return flag
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        minutes = 0
        while self.markRotten(grid, m ,n):
            minutes += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minutes