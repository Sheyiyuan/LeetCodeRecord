// Problem: https://leetcode.cn/problems/find-the-highest-altitude/
// Accepted at: 2026年6月19日 21:30

function largestAltitude(gain: number[]): number {
    let largestAltitude = 0;
    let curAltitude = 0;
    for (let i = 0; i < gain.length; i++) {
        curAltitude += gain[i];
        largestAltitude = Math.max(curAltitude, largestAltitude);
    }
    return largestAltitude;
};
