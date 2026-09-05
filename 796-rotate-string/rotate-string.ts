// Problem: https://leetcode.cn/problems/rotate-string/
// Accepted at: 2026年5月3日 09:54

function rotateString(s: string, goal: string): boolean {
    if (!(s.length === goal.length)) {
        return false;
    }
    if (s.length === 1 && s === goal) {
        return true
    }
    for (let i = 0; i < s.length; i++) {
        s = rotate(s);
        if (s === goal) {
            return true;
        }
    }
    return false;

};

function rotate(s: string): string {
    return s.slice(-(s.length - 1)) + (s[0]);
}
