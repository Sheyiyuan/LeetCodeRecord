// Problem: https://leetcode.cn/problems/number-of-strings-that-appear-as-substrings-in-word/
// Accepted at: 2026年6月29日 11:22

function numOfStrings(patterns: string[], word: string): number {
    let totalSubString: number = 0;
    for (let i = 0; i < patterns.length; i++){
        let curPattern = patterns[i];
        if (isSubString(curPattern,word)){
            totalSubString += 1;
        }
    }
    return totalSubString;
};

function isSubString(pattern: string,word: string) {
    return word.includes(pattern)
}
