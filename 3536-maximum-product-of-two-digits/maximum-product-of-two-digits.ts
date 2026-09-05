// Problem: https://leetcode.cn/problems/maximum-product-of-two-digits/
// Accepted at: 2026年7月25日 23:06

function maxProduct(n: number): number {
    let FirstMaxNum = 0;
    let SecondMaxNum = 0;
    while (n > 0) {
        const curNum = n % 10;
        if (curNum > FirstMaxNum) {
            SecondMaxNum = FirstMaxNum;
            FirstMaxNum = curNum;
        } else if (curNum > SecondMaxNum) {
            SecondMaxNum = curNum;
        } 
        n = (n - curNum) / 10;
    }
    return FirstMaxNum * SecondMaxNum;
};
