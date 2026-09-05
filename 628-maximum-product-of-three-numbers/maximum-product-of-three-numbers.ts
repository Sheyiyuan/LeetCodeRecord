// Problem: https://leetcode.cn/problems/maximum-product-of-three-numbers/
// Accepted at: 2026年7月26日 09:45

function maximumProduct(nums: number[]): number {
    let firstMaxNum = -Infinity;
    let secondMaxNum = -Infinity;
    let thridMaxNum = -Infinity;
    let firstMinNum = Infinity;
    let secondMinNum = Infinity;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > firstMaxNum) {
            thridMaxNum = secondMaxNum;
            secondMaxNum = firstMaxNum;
            firstMaxNum = nums[i];
        } else if (nums[i] > secondMaxNum) {
            thridMaxNum = secondMaxNum;
            secondMaxNum = nums[i];
        } else if (nums[i] > thridMaxNum) {
            thridMaxNum = nums[i];
        }
        if (nums[i] < firstMinNum) {
            secondMinNum = firstMinNum;
            firstMinNum = nums[i];
        } else if (nums[i] < secondMinNum) {
            secondMinNum = nums[i];
        }
    }
    return Math.max(firstMaxNum * secondMaxNum * thridMaxNum, firstMaxNum * firstMinNum * secondMinNum);
};
