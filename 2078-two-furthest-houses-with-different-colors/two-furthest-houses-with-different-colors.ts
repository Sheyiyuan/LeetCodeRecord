// Problem: https://leetcode.cn/problems/two-furthest-houses-with-different-colors/
// Accepted at: 2026年4月20日 11:04

function maxDistance(colors: number[]): number {
    let maxDistence = 0;

    for (let i = 0; i < colors.length; i++) {
        const lastColor = colors[colors.length - 1];
        const curColor = colors[i];
        if (curColor !== lastColor) {
            maxDistence = Math.max(maxDistence, colors.length - i - 1);
            break;
        }
    }

    for (let j = colors.length - 1; j > 0; j--) {
        const lastColor = colors[j];
        const curColor = colors[0];
        if (curColor !== lastColor) {
            maxDistence = Math.max(maxDistence, j);
            break;
        }
    }

    return maxDistence;
};
