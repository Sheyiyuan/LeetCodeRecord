// Problem: https://leetcode.cn/problems/remove-element/
// Accepted at: 2025年3月4日 09:04

func removeElement(nums []int, val int) int {
    p1:=0
    p2:=len(nums)-1
    k:=len(nums)
    for p1<=p2{
        if nums[p2]==val{
            p2--
            k--
            continue
        }
        if nums[p1]==val{
            nums[p1]=nums[p2]
            p2--
            k--
            continue
        }else{
            p1++
        }
    }
    return k
}
