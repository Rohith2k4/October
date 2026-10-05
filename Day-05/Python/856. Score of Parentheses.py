from itertools import accumulate
class Solution:
    def scoreOfParentheses(self, s: str) -> int: return sum(1 << depth for i, depth in enumerate(accumulate(1 if c == "(" else -1 for c in s)) if s[i] == ")" and s[i - 1] == "(")
