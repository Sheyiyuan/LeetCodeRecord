// Problem: https://leetcode.cn/problems/maximum-product-of-two-elements-in-an-array/
// Accepted at: 2026年7月27日 17:33

function maxProduct(nums: number[]): number {
    let firstMaxNum = 0;
    let secondMaxNum = 0;
    for (let i = 0; i < nums.length; i++) {
        const curNum = nums[i];
        if (curNum > firstMaxNum) {
            secondMaxNum = firstMaxNum;
            firstMaxNum = curNum;
        } else if (curNum > secondMaxNum) {
            secondMaxNum = curNum;
        }
    }
    return (firstMaxNum - 1) * (secondMaxNum - 1);
};
