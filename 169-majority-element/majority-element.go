// Problem: https://leetcode.cn/problems/majority-element/
// Accepted at: 2025年3月4日 11:11

func majorityElement(nums []int) int {
    numsMap:=make(map[int]int)
    for _,v := range nums{
        numsMap[v]++
        if numsMap[v]>len(nums)/2{
            return v
        }
    }
    return 0
}
