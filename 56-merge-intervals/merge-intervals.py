# Problem: https://leetcode.cn/problems/merge-intervals/
# Accepted at: 2026年8月31日 22:09

"""
# 思路说明
我们维护一个变量 `cur` 用于显示当前的区间，`next` 用于读取下一个区间，然后比较两个区间是否重叠，如果重叠，把两者合并，否则 `cur` 存入合并后的结果，把 `next` 作为新的 `cur`，然后重复上述过程。
为了合并有序，我们需要先进行排序。
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=itemgetter(0))

        cur = intervals[0]
        result = []

        for i in range(1,len(intervals)):
            next = intervals[i]
            if cur[1] >= next[0] :
                cur[1] = max(cur[1],next[1])
            else:
                result.append(cur)
                cur = next
        
        result.append(cur)

        return result
