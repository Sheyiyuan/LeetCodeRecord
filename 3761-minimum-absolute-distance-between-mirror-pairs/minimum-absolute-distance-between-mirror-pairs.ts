// Problem: https://leetcode.cn/problems/minimum-absolute-distance-between-mirror-pairs/
// Accepted at: 2026年4月17日 11:43

function minMirrorPairDistance(nums: number[]): number {
    let result = Infinity;
    const record = new Map<number, number>();

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const rev = reverse(num);

        if (record.has(num)) {
            const prevIndex = record.get(num)!;
            result = Math.min(Math.abs(i - prevIndex), result);
        }

        record.set(rev, i);
    }

    return result === Infinity ? -1 : result;
}

function reverse(num: number): number {
    let res = 0;
    while (num > 0) {
        res = res * 10 + num % 10;
        num = Math.floor(num / 10);
    }
    return res;
}
