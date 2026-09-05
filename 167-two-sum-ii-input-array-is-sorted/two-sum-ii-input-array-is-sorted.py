# Problem: https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
# Accepted at: 2026年8月30日 08:34

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum > target:
                j = j-1
            elif sum < target:
                i = i+1
            else:
                return [i+1,j+1]
        return []
