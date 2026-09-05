// Problem: https://leetcode.cn/problems/group-anagrams/
// Accepted at: 2026年4月17日 14:19

function groupAnagrams(strs: string[]): string[][] {
    const record = new Map<string,string[]>();
    const result: string[][] = [];
    const ids: string[] = [];

    for (let i =0; i < strs.length; i++){
        const curStr = strs[i];
        const id = sort(curStr);
        
        if(!record.has(id)){
            ids.push(id);
            record.set(id,[curStr]);
            continue;
        }

        const curStrs = record.get(id);
        curStrs.push(curStr);
        record.set(id,curStrs)
    }

    for (let i =0; i < ids.length; i++){
        result.push(record.get(ids[i]));
    }

    return result
};

function sort(str: string):string {
    const strArray = str.split("");
    strArray.sort();
    return strArray.join("");
}
