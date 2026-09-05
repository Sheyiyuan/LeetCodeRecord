// Problem: https://leetcode.cn/problems/rotate-image/
// Accepted at: 2026年5月4日 20:12

/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
    const tmpMatrix: number[][] = JSON.parse(JSON.stringify(matrix));
    const n: number = matrix.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            matrix[i][j] = tmpMatrix[n - 1 - j][i]
        }
    }
};
