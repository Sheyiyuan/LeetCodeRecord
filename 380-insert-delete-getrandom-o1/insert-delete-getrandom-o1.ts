// Problem: https://leetcode.cn/problems/insert-delete-getrandom-o1/
// Accepted at: 2026年3月2日 10:44

class RandomizedSet {
    elems:Map<any, boolean>;

    constructor() {
        this.elems = new Map<any, boolean>;
    }

    insert(val: number): boolean {
        let res = this.elems.has(val);
        this.elems.set(val,true);
        return !res
    }

    remove(val: number): boolean {
        let res = this.elems.has(val);
        this.elems.delete(val);
        return res
    }

    getRandom(): number {
        const vals = Array.from( this.elems.keys() );
        return vals[Math.floor(Math.random() * vals.length)];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
