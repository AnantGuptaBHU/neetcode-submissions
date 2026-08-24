class Solution:
    def fun(self, n, s, res, open, close):
        if (open + close) == 2*n and open == close:
            res.append(s)
            return
        if close > open or len(s) == 2*n:
            return
        self.fun(n, s+'(', res, open+1, close)
        self.fun(n, s+')', res, open, close+1)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.fun(n, '', res, 0, 0)
        return res