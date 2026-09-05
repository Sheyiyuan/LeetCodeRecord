// Problem: https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/
// Accepted at: 2025年3月4日 11:02

func removeDuplicates(nums []int) int {
    if len(nums)<3{
        return len(nums)
    }
    p1:=2
    p2:=2
    for p2<len(nums){
        if nums[p2]!=nums[p1-2]{
            nums[p1]=nums[p2]
            p1++
        }
        p2++
    }
    return p1
}
