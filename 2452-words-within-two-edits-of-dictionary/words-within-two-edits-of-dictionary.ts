// Problem: https://leetcode.cn/problems/words-within-two-edits-of-dictionary/
// Accepted at: 2026年4月22日 11:09

function twoEditWords(queries: string[], dictionary: string[]): string[] {
    const result: string[] = [];
    for (let i = 0; i < queries.length; i++) {
        for (let j = 0; j < dictionary.length; j++) {
            if (compareAreTheyFit(queries[i], dictionary[j])) {
                result.push(queries[i]);
                break;
            }
        }
    }
    return result;
};

function compareAreTheyFit(qWord: string, dWord: string): boolean {
    const qArray: string[] = qWord.split("");
    const dArray: string[] = dWord.split("");
    let err: number = 0;

    for (let i = 0; i < qArray.length; i++) {
        if (qArray[i] !== dArray[i]) {
            err += 1;
        }
    }

    return err <= 2 ? true : false;
}
