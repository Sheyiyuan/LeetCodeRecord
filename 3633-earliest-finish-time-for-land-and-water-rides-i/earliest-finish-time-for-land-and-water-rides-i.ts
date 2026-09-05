// Problem: https://leetcode.cn/problems/earliest-finish-time-for-land-and-water-rides-i/
// Accepted at: 2026年6月2日 14:05

function earliestFinishTime(landStartTime: number[], landDuration: number[], waterStartTime: number[], waterDuration: number[]): number {
    const landTotal: number = landStartTime.length;
    const waterTotal: number = waterStartTime.length;
    let earliestEndTime: number = Infinity;
    for (let i = 0; i < landTotal; i++) {
        const curLandStart: number = landStartTime[i];
        const curLandEnd: number = curLandStart + landDuration[i];
        for (let j = 0; j < waterTotal; j++) {
            const curWaterStart: number = waterStartTime[j];
            const curWaterEnd: number = curWaterStart + waterDuration[j];
            if (curLandEnd <= curWaterStart) {
                earliestEndTime = Math.min(earliestEndTime, curWaterEnd);
            } else {
                earliestEndTime = Math.min(earliestEndTime, curLandEnd + waterDuration[j]);
            }
            if (curWaterEnd <= curLandStart) {
                earliestEndTime = Math.min(earliestEndTime, curLandEnd);
            }else{
                earliestEndTime = Math.min(earliestEndTime, curWaterEnd + landDuration[i]);
            }
        }
    }
    return earliestEndTime;
};
