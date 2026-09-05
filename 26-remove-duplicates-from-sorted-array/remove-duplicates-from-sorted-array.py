# Problem: https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
# Accepted at: 2026年8月30日 12:23

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
