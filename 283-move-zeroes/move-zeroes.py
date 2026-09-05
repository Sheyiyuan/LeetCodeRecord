# Problem: https://leetcode.cn/problems/move-zeroes/
# Accepted at: 2026年8月28日 10:36

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        
        for j in range(len(nums)) :
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        
        while i < len(nums):
            nums[i] = 0
            i += 1
