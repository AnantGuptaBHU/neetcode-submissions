class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for no in range(n//2):
            fr = fc = no
            lr = lc = n-no-1
            for i in range(lc-fc):
                a = matrix[fr][fc+i]
                b = matrix[fc+i][lc]
                matrix[fc+i][lc] = a
                c = matrix[lr][lc - i]
                matrix[lr][lc - i] = b
                d = matrix[lr-i][fc]
                matrix[lr-i][fc] = c
                matrix[fr][fc+i] = d
        return 