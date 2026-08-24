class Solution:
    def sq(self, n):
        s = 0
        while n:
            a=n%10
            s+=a*a
            n//=10
        return s
    def isHappy(self, n: int) -> bool:
        d=set()
        d.add(n)
        while n != 1:
            n=self.sq(n)
            if n in d:
                return False
            else:
                d.add(n)
        return True

        