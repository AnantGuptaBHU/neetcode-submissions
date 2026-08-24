class Solution:
    def spiralOrder(self, matrix) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        i = j = 0
        ii = m
        jj = n
        res = []
        while j < jj and i < ii:
            for jjj in range(j, jj):
                res.append(matrix[i][jjj])
            i += 1
            for iii in range(i, ii):
                res.append(matrix[iii][jj - 1])
            jj -= 1
            if i < ii:
                for jjj in range(jj - 1, j - 1, -1):
                    res.append(matrix[ii - 1][jjj])
                ii -= 1
            if j < jj:
                for iii in range(ii - 1, i - 1, -1):
                    res.append(matrix[iii][j])
                j += 1
        return res