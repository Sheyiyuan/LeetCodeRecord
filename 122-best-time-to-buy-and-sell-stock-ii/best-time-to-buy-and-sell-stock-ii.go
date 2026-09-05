// Problem: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
// Accepted at: 2025年3月5日 17:34

func maxProfit(prices []int) int {
    max:=0
    for i:=1;i<len(prices);i++{
        if prices[i-1]<prices[i]{
            max+=prices[i]-prices[i-1]
        }
    }
    return max
}
