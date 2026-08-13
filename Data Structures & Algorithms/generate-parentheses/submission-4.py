class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtrack(opn, clsd):

            if opn == clsd == n:
                res.append("".join(stack))
                return

            if opn < n:
                stack.append("(")
                backtrack(opn + 1, clsd)
                stack.pop()

            if clsd < opn:
                stack.append(")")
                backtrack(opn, clsd + 1)
                stack.pop()

        backtrack(0, 0)
        return res             


        