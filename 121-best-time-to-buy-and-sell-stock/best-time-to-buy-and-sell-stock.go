// Problem: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
// Accepted at: 2025年3月5日 17:16

func maxProfit(prices []int) int {
    max:=0
    min:=prices[0]
    for i:=0;i<len(prices);i++{
        if prices[i]<min{
            min=prices[i]
        }
        if prices[i]-min>=max{
            max=prices[i]-min
        }
    }
    return max
}
