class Solution:
    def return_opp(self, c):
        if c == '(':
            return ')'
        if c == ')':
            return '('
        if c =='[':
            return ']'
        if c == ']':
            return '['
        if c =='{':
            return '}'
        if c == '}':
            return '{'
    def isValid(self, s: str) -> bool:
        st = []
        l = len(s)
        o = ['(', '{', '[']
        for c in s:
            if c in o:
                st.append(c)
            else:
                if len(st) == 0:
                    return False
                a = st.pop()
                if a != self.return_opp(c):
                    return False
        if len(st) != 0:
            return False
        return True
        