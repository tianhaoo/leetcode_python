# 160. 相交链表
from Utils import ListNode, deserialize_linked_list


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        p1 = tail1 = headA
        p2 = tail2 = headB
        n1 = n2 = 0
        while tail1:
            tail1 = tail1.next
            n1 += 1
        while tail2:
            tail2 = tail2.next
            n2 += 1
        if n1 > n2:
            for i in range(n1-n2):
                p1 = p1.next
        else:
            for i in range(n2-n1):
                p2 = p2.next
        if p1 == p2:
            return p1
        elif p1.next is None and p2.next is None:
            return None
        else:
            while p1 and p2:
                if p1.next == p2.next:
                    return p1.next
                p1 = p1.next
                p2 = p2.next

        return None







if __name__ == '__main__':
    s = Solution()
    intersectVal = 1
    listA = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    listB = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    skipA = 0
    skipB = 0

    head1 = deserialize_linked_list(listA)
    head2 = deserialize_linked_list(listB)
    if not intersectVal:
        p1 = head1
        for i in range(skipA-1):
            p1 = p1.next
        p2 = head2
        for i in range(skipB):
            p2 = p2.next
        p1.next = p2

    print(head1)
    print(head2)

    print(s.getIntersectionNode(head1, head1))