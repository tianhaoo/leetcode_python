# 876. 链表的中间结点
from Utils import ListNode, deserialize_linked_list


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head

        p1 = p2 = dummy
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        return p1.next

if __name__ == '__main__':
    s = Solution()
    head = [1, 2, 3, 4, 5]
    print(s.middleNode(deserialize_linked_list(head)))