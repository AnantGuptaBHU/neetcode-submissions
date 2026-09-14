class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        l1 = len(num1)
        unit = 0
        for i in range(l1-1, -1, -1):
            a = ord(num1[i]) - 48
            n1 = ((10 ** unit) * a) + n1
            unit+=1
        n2 = 0
        l2 = len(num2)
        unit = 0
        for i in range(l2-1, -1, -1):
            a = ord(num2[i]) - 48
            n2 = ((10 ** unit) * a) + n2
            unit+=1
        return str(n1*n2)