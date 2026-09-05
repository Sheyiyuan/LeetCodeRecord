# Problem: https://leetcode.cn/problems/subarray-sum-equals-k/
# Accepted at: 2026年8月30日 15:41

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        pre_sums = {0:1}
        pre_sum = 0
        for num in nums:
            pre_sum += num
            complement = pre_sum - k
            if complement in pre_sums:
                total += pre_sums[complement]
            pre_sums[pre_sum] = pre_sums.get(pre_sum,0) + 1
        return total
