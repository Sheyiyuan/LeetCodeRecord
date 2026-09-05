# Problem: https://leetcode.cn/problems/maximum-subarray/
# Accepted at: 2026年8月30日 15:54

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_sum = 0
        min_pre_sum = 0
        max_pre_sum = -float('inf')
        for i in range(len(nums)):
            pre_sum += nums[i]
            max_pre_sum = max(max_pre_sum,pre_sum-min_pre_sum)
            min_pre_sum = min(min_pre_sum,pre_sum)
        return max_pre_sum
