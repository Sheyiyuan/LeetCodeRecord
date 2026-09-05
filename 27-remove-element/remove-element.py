# Problem: https://leetcode.cn/problems/remove-element/
# Accepted at: 2026年8月29日 16:55

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == val:
                i = i + 1
            else:
                nums[j] = nums[i]
                i = i + 1
                j = j + 1
                k = k + 1
        return k
