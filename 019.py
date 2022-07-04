# 19. 删除链表的倒数第 N 个结点
from Utils import ListNode, deserialize_linked_list


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        p1 = p2 = dummy
        for i in range(n):
            p2 = p2.next
        # if not p2:
        #     return p1.next
        while p2:
            if not p2.next:
                p1.next = p1.next.next
                break
            else:
                p1 = p1.next
                p2 = p2.next
        return dummy.next




if __name__ == '__main__':
    s = Solution()
    head = [1, 2, 3, 4, 5]
    n = 2
    # head = [1, 2]
    # n = 2
    print(s.removeNthFromEnd(deserialize_linked_list(head), n))