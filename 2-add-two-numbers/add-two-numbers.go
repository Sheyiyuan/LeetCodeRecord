// Problem: https://leetcode.cn/problems/add-two-numbers/
// Accepted at: 2025年3月9日 19:13

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    result := &ListNode{}
    tmp := result
    carry:=0
    for l1 !=nil || l2 !=nil || carry!=0{
        v1,v2:=0,0
        if l1 != nil {
            v1=l1.Val
            l1=l1.Next
        }
        if l2 != nil{
            v2=l2.Val
            l2=l2.Next
        }
        sum:=v1+v2+carry
        tmp.Next=&ListNode{Val:sum%10}
        tmp=tmp.Next
        carry=sum/10
    }
    return result.Next
}
