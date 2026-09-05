# Problem: https://leetcode.cn/problems/linked-list-cycle-ii/
# Accepted at: 2026年9月4日 11:52

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        else:
            return None
        
        fast = head

        while True:
            if slow == fast:
                return fast
            fast = fast.next
            slow = slow.next
