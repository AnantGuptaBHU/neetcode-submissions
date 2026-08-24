class Solution:
    def setZero(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        return 1 + self.setZero(grid, i+1, j, m, n) + self.setZero(grid, i-1, j, m, n) + self.setZero(grid, i, j+1, m, n) + self.setZero(grid, i, j-1, m, n)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m  = len(grid)
        n = len(grid[0])
        maxi = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxi = max(maxi, self.setZero(grid, i, j, m, n))
        return maxi