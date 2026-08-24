class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        r = [0] * n
        stack = []
        for i in range(n):
            while len(stack) > 0 and temp[stack[-1]] < temp[i]:
                a = stack.pop()
                r[a] = i - a
            stack.append(i)
        return r