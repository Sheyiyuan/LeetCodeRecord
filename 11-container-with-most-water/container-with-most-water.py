# Problem: https://leetcode.cn/problems/container-with-most-water/
# Accepted at: 2026年8月28日 10:50

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_S = 0

        while i < j:
            cur_height = min(height[i],height[j])
            cur_S = (j - i) * cur_height
            max_S = max(cur_S,max_S)
            if height[i] <= height[j]:
                i = i + 1
            else :
                j = j - 1
        
        return max_S
