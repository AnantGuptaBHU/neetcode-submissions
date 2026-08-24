class Solution:
    def setZero(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.setZero(grid, i+1, j, m, n)
        self.setZero(grid, i-1, j, m, n)
        self.setZero(grid, i, j+1, m, n)
        self.setZero(grid, i, j-1, m, n)

    def numIslands(self, grid):
        m  = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.setZero(grid, i, j, m, n)
                    count+=1
        return count