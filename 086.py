# 86. 分隔链表
from Utils import ListNode, deserialize_linked_list, print_linked_list


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p = head
        small_dummy = ListNode()
        large_dummy = ListNode()
        p_small = small_dummy
        p_large = large_dummy
        while p:
            if p.val < x:
                p_small.next = ListNode(p.val)
                p_small = p_small.next
            else:
                p_large.next = ListNode(p.val)
                p_large = p_large.next
            p = p.next
        p_small.next = large_dummy.next
        return small_dummy.next



if __name__ == '__main__':
    s = Solution()
    head = [1, 4, 3, 2, 5, 2]
    x = 3
    head = s.partition(deserialize_linked_list(head), x)
    print_linked_list(head)