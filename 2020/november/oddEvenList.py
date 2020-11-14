from define.ListNode import ListNode

# 来源 https://leetcode-cn.com/problems/odd-even-linked-list/
# 官方题解
def oddEvenList_official(head: ListNode) -> ListNode:
    if not head:
        return head

    evenHead = head.next
    odd, even = head, evenHead
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = evenHead
    return head

# 将奇数节点排在一起，再排偶数节点
def oddEvenList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    oddList = []
    evenList = []
    count = 1
    result = head
    temp = result
    while head:
        if count % 2 == 0:
            evenList.append(head.val)
        else:
            oddList.append(head.val)
        head = head.next
        count += 1
    for odd in oddList:
        temp.next = ListNode(val=odd)
        temp = temp.next
    for even in evenList:
        temp.next = ListNode(val=even)
        temp = temp.next
    return result.next


if __name__ == '__main__':

    listnode = ListNode(val=2, next=ListNode(val=1, next=ListNode(3, next=ListNode(val=4))))
    result = oddEvenList(listnode)
    while result:
        print(result.val)
        result = result.next