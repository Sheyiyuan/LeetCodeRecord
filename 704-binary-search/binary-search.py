# Problem: https://leetcode.cn/problems/binary-search/
# Accepted at: 2026年8月30日 13:10

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n
        while left < right:
            cur = left+(right-left)//2
            if target > nums[cur] :
                left = cur + 1
            elif target < nums[cur]:
                right = cur
            else: 
                return cur
        return -1
