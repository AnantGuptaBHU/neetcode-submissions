class Solution:
    def reverse(self, x):
        ans = 0
        flag = True
        if x < 0:
            flag = False
        xx = x if flag else (-1) * x
        while xx:
            a = xx % 10
            ans = a + (ans*10)
            xx = xx//10
        if flag == False:
            ans = (-1) * ans
        print(ans)
        if (-2**31) <= ans <= (2**31 - 1):
            return ans  
        else:
            return 0