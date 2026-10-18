class Solution:

    def setXX(self, grid, i, j, m, n):
        stack = [(i, j)]
        surrounded = True
        while stack:
            i, j = stack.pop()
            if grid[i][j] != 'O':
                continue
            # If this O is on boundary, region is NOT surrounded
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                surrounded = False
                continue
            grid[i][j] = 'XX'
            # Add neighbours
            if i + 1 < m and grid[i+1][j] == 'O':
                stack.append((i+1, j))
            if i - 1 >= 0 and grid[i-1][j] == 'O':
                stack.append((i-1, j))
            if j + 1 < n and grid[i][j+1] == 'O':
                stack.append((i, j+1))
            if j - 1 >= 0 and grid[i][j-1] == 'O':
                stack.append((i, j-1))
        return surrounded


    def markBack(self, grid, surrounded):
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'XX':
                    grid[i][j] = 'X' if surrounded else 'O'


    def solve(self, grid):
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'O':
                    surrounded = self.setXX(grid, i, j, m, n)
                    self.markBack(grid, surrounded)