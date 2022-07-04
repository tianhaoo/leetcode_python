# 141. 环形链表
from typing import Optional

from Utils import ListNode, deserialize_linked_list


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p1 = p2 = head
        while p2.next and p2.next.next:

            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    lst = []
    pos = -1
    head = deserialize_linked_list(lst)
    p = tail = head
    while p and p.next:
        tail = p.next
        p = p.next
    if pos != -1:
        node = head
        for i in range(pos):
            node = node.next
        tail.next = node

    print(head)

    print(s.hasCycle(head))