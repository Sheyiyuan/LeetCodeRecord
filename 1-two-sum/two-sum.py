# Problem: https://leetcode.cn/problems/two-sum/
# Accepted at: 2026年8月30日 10:51

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            cur = nums[i]
            complement = target - cur
            if complement in map and map[complement] != i:
                return [map[complement],i]
            else:
                map[cur] = i
        
        return []
