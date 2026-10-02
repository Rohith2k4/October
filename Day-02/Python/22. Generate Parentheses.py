class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return [""] if n == 0 else ["(" + left + ")" + right for i in range(n) for left in self.generateParenthesis(i) for right in self.generateParenthesis(n - 1 - i)]
