# Problem: https://leetcode.cn/problems/first-missing-positive/
# Accepted at: 2026年9月1日 11:51

"""
用「归位」实现
把每个下标的位置放上下标加一对应的数就是归位，我们只要找到不能被归位的首个下标，那么就找到了没有出现过的最小正整数
相当于用下标代替 HashMap 的 key 来实现记忆
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            cur = nums[i]
            if cur == i+1: # 已归位
                i +=1
            elif cur > 0 and cur <= n and nums[cur-1] != nums[i]: # 满足可归位条件则归位
                nums[i] = nums[cur-1]
                nums[cur-1] = cur
            else: # 不满足可归位条件则跳过
                i +=1
        
        # 重新遍历找出未归位的元素并返回：
        for j in range(n):
            if j+1 != nums[j]:
                return j+1
        
        return n+1
