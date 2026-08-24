class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # CGT
        d = {}
        left = maxi = 0
        for right in range(len(s)):
            if s[right] in d:
                left = max(left, d[s[right]]+1)
            d[s[right]] = right
            maxi = max(maxi, right - left + 1)
        return maxi