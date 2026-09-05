// Problem: https://leetcode.cn/problems/shortest-distance-to-target-string-in-a-circular-array/
// Accepted at: 2026年4月15日 12:45

function closestTarget(words: string[], target: string, startIndex: number): number {
    const n = words.length;
    let result = 101;
    let has_target = false;
    for(let i = 0; i < n; i++){
        if (words[i] === target){
            has_target = true;
            result = Math.min(result,Math.abs(i - startIndex),n - Math.abs(i - startIndex));
        }
    }
    if (has_target){
        return result;
    }
    return -1;
};
