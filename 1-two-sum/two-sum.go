// Problem: https://leetcode.cn/problems/two-sum/
// Accepted at: 2025年3月9日 18:33

func twoSum(nums []int, target int) []int {
    result:=make([]int,2)
    tmp:=make(map[int]int)
    for i:=0;i<len(nums);i++{
        delta:=target-nums[i]
        index,ok:=tmp[delta]
        if ok && i!=index {
            result[0]=i
            result[1]=index
            return result
        }
        tmp[nums[i]]=i
    }
    return result
}
