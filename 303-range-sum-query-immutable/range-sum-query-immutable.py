# Problem: https://leetcode.cn/problems/range-sum-query-immutable/
# Accepted at: 2026年8月30日 14:09

class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = []
        cur_pre_sum = 0
        for item in nums:
            cur_pre_sum += item
            self.pre_sum.append(cur_pre_sum)
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pre_sum[right]
        return self.pre_sum[right] - self.pre_sum[left - 1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
