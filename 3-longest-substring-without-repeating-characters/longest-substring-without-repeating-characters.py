# Problem: https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# Accepted at: 2026年8月30日 12:06

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        fast = 0
        max_len = 0
        record = set()
        while fast < len(s):
            cur_left = s[slow]
            cur_right = s[fast]
            if cur_right in record:
                slow = slow +1
                record.remove(cur_left)
            else:
                record.add(cur_right)
                fast = fast + 1
                max_len = max(max_len, len(record))
        return max_len
