class Solution:
    def cal(self, s1, s2, op):
        if op == '+':
            return str(int(s1) + int(s2))
        if op == '*':
            return str(int(s1) * int(s2))
        if op == '-':
            return str(int(s1) - int(s2))
        if op == '/':
            return str(int(int(s1) / int(s2)))
    def evalRPN(self, tokens: List[str]) -> int:
        r = 0
        l = len(tokens)
        ops = ['+','-','*','/']
        stack = []
        for i in range(l):
            if tokens[i] in ops:
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(self.cal(s1, s2, tokens[i]))
            else:
                stack.append(tokens[i])
            # print(l,i,stack)
        return int(stack[-1])