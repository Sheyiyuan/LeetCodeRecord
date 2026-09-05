// Problem: https://leetcode.cn/problems/rotate-array/
// Accepted at: 2025年3月4日 15:04

func rotate(nums []int, k int)  {
    k=k%len(nums)
    n:=len(nums)-1
    reverse(nums,0,n)
    reverse(nums,0,k-1)
    reverse(nums,k,n)
}

func reverse (nums []int, start, end int){
    for start<end {
        tmp:=nums[start]
        nums[start]=nums[end]
        nums[end]=tmp
        start++
        end--
    }
}
