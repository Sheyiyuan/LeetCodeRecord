// Problem: https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
// Accepted at: 2025年3月4日 10:10

func removeDuplicates(nums []int) int {
    p1:=0
    p2:=1
    k:=1
    for p1<=len(nums)-1&&p2<=len(nums)-1{
        if nums[p1] == nums[p2]{
            p2++
        }else if nums[p2]==nums[p2-1]{
            p2++
        }else{
            nums[p1+1]=nums[p2]
            p1++
            k++
        }
    }
    return k
}
