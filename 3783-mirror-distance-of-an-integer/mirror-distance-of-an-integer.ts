// Problem: https://leetcode.cn/problems/mirror-distance-of-an-integer/
// Accepted at: 2026年4月18日 00:52

function mirrorDistance(n: number): number {
    return Math.abs(n - reverse(n));
};

function reverse(n: number): number {
    let rev = 0;
    for (let i = n; i > 0; i = Math.floor(i / 10)) {
        rev = rev * 10 + i % 10;
    }
    return rev;
}
