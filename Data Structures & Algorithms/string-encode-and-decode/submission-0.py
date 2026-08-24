class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s = s + '#' + str(len(word)) + '#' + word
        return s

    def decode(self, s: str) -> List[str]:
        l = len(s)
        r = []
        i = 0
        while i < l:
            # if s[i] == '#' and s[i+1].isnumeric():
            ll = s[i+1]
            i+=2
            while s[i]!='#':
                ll = ll + s[i]
                i+=1
            i+=1
            lll = int(ll)
            r.append(s[i:i+lll])
            i+=lll
        return r

            