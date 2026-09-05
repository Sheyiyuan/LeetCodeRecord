# Problem: https://leetcode.cn/problems/daily-temperatures/
# Accepted at: 2026年9月4日 21:27

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调栈
        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        
        return answer
