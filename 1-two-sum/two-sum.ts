// Problem: https://leetcode.cn/problems/two-sum/
// Accepted at: 2026年6月29日 18:49

function twoSum(nums: number[], target: number): number[] {
    const indexRecord = new Map<number, number>;
    for (let i = 0; i < nums.length; i++) {
        let curNum = nums[i];
        let curTargetNum = target - curNum;
        let curTargetNumIndex = indexRecord.get(curTargetNum);
        if (curTargetNumIndex === undefined) {
            indexRecord.set(curNum,i);
            continue;
        }
        return [i,curTargetNumIndex]
    }
};
