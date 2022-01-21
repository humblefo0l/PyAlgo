from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        o = n
        c = n
        bal = []

        return self._generateParanthesis(o, c, bal, "")

    def _generateParanthesis(self, o, c, bal, current) -> List[str]:
        if o <= 0 and c > 0:
            c1 = current + ")"
            self._generateParanthesis(o, c - 1, bal, c1)

        if o > 0 and c < 0:
            return bal

        if o == 0 and c == 0:
            bal.append(current)
            return bal

        if o > 0 and c > 0:
            if o == c:
                c1 = current + "("
                self._generateParanthesis(o - 1, c, bal, c1)

            if o < c:
                c1 = current + "("
                self._generateParanthesis(o - 1, c, bal, c1)
                c2 = current + ")"
                self._generateParanthesis(o, c - 1, bal, c2)

            if o > c:
                c1 = current + ")"
                self._generateParanthesis(o, c - 1, bal, c1)

        return bal

s = Solution()
print(s.generateParenthesis(3))
print(s.generateParenthesis(1))
print(s.generateParenthesis(10))