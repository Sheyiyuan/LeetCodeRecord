# Problem: https://leetcode.cn/problems/corporate-flight-bookings/
# Accepted at: 2026年8月31日 10:07

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 定义一个差分数组用于记录变化
        diff = [0] * n
        anwser = [0] * n
        for first,last,seats in bookings:
            diff[first-1] += seats
            if last < n:
                diff[last] -= seats
        
        for i in range(1, n):
            diff[i] += diff[i-1]
        return diff
