class Solution:
    def longestPalindrome(self, s: str) -> str:
        lc =rc = 0
        l = len(s)
        maxi = 0
        maxi_substring = ''
        for i in range(0, l):
            j = i-1
            k = i+1
            count_odd = 1
            while j >= 0 and k < l and s[j] == s[k]:
                count_odd += 2
                j-=1
                k+=1
            if count_odd > maxi:
                maxi = count_odd
                maxi_substring = s[j+1:k]
            lc = i
            rc = i+1
            count_even = 0
            while lc >=0 and rc<l and s[lc] == s[rc]:
                count_even += 2
                lc -=1
                rc+=1
            if count_even > maxi:
                maxi = count_even
                maxi_substring = s[lc+1:rc]
        return maxi_substring