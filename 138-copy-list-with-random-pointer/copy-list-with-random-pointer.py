# Problem: https://leetcode.cn/problems/copy-list-with-random-pointer/
# Accepted at: 2026年9月5日 11:37

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur = head
        map = {}
        while cur:
            map[cur] = Node(cur.val,None,None)
            cur = cur.next
        
        for origin in map:
            copied = map[origin]
            if origin.next:
                copied.next = map[origin.next]
            if origin.random:
                copied.random = map[origin.random]
        
        return map[head]
