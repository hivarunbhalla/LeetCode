class Solution:
    def removeStars(self, s: str) -> str:
        stk = []

        for i in s:
            if i == '*' and len(stk):
                stk.pop()

            else:
                stk.append(i)

        return ''.join(stk)