class Solution:
    def countSubstrings(self, s: str) -> int:
        lc =rc = 0
        l = len(s)
        total_count = 0
        for i in range(0, l):
            j = i-1
            k = i+1
            total_count += 1
            while j >= 0 and k < l and s[j] == s[k]:
                j-=1
                k+=1
                total_count += 1
            lc = i
            rc = i+1
            while lc >=0 and rc<l and s[lc] == s[rc]:
                lc -=1
                rc+=1
                total_count += 1
        return total_count