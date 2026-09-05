// Problem: https://leetcode.cn/problems/jump-game/
// Accepted at: 2025年3月5日 17:47

func canJump(nums []int) bool {
    max:=0
    for i:=0;i<len(nums);i++{
        if max<i{
            return false
        }
        if max<i+nums[i] {
            max=i+nums[i]
        }
    }
    return true
}
