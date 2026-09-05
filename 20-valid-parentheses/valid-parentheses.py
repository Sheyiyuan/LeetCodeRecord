# Problem: https://leetcode.cn/problems/valid-parentheses/
# Accepted at: 2026年9月4日 19:48

class Solution:
    def isValid(self, s: str) -> bool:
        matching = {'(':')','[':']','{':'}'}
        stack = []

        for char in s:
            if not char in matching:
                # 空栈遇到右括号直接 false
                if len(stack) == 0:
                    return False
                elif matching[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        return False
