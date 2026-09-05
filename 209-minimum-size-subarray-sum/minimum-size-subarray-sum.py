# Problem: https://leetcode.cn/problems/minimum-size-subarray-sum/
# Accepted at: 2026年8月30日 10:58

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        length = float('inf')
        n = len(nums)
        total = 0
        for fast in range(n) :
            total = total + nums[fast]
            while total >= target:
                length = min(length, fast-slow+1)
                total = total - nums[slow]
                slow = slow + 1
        
        if length > n :
            return 0
        return length
