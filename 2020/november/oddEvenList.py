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


def oddEvenList(head: ListNode) -> ListNode:
    if head is None:
        return None
    if head.next is None:
        return head
    arr = []
    count = 1
    temp = head
    while temp is not None:
        # arr.append(head.val)
        # head = head.next
        if temp.val % 2 == 0 and count % 2 == 0:
            temp = head.next
            count += 1
        elif temp.val % 2 != 0 and count % 2 != 0:
            temp = head.next
            count += 1
        else:
            arr.append(temp.val)
            temp = head.next

        print(count)
    print(arr)
    return None


if __name__ == '__main__':

    listnode = ListNode(val=2, next=ListNode(val=1, next=ListNode(3, next=ListNode(val=4))))
    result = oddEvenList_official(listnode)
    while result:
        print(result.val)
        result = result.next