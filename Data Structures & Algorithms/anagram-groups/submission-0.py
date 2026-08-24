class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for st in strs:
            a = [0]*26
            for c in st:
                a[ord(c) - 97] += 1
            a = tuple(a)
            if a in d:
                d[a].append(st)
            else:
                d[a] = [st]
        return list(d.values())