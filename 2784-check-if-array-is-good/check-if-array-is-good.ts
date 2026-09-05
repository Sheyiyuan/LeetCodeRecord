// Problem: https://leetcode.cn/problems/check-if-array-is-good/
// Accepted at: 2026年5月14日 21:05

function isGood(nums: number[]): boolean {
    const n = nums.length - 1;
    const record = new Map<number, number>();
    for (let i = 0; i <= n; i++) {
        const curNum = nums[i];
        if (curNum > n) {
            return false;
        }
        const curRecord = (record.get(curNum) ?? 0) + 1;
        record.set(curNum, curRecord);
        if ((curRecord > 1 && curNum !== n) || (curRecord > 2)) {
            return false;
        }
    }
    return true;
};
