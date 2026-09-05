# Problem: https://leetcode.cn/problems/remove-linked-list-elements/
# Accepted at: 2026年9月3日 17:55

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        cur = head

        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                prev = prev.next
        
        return dummy.next
