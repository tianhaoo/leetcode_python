# 21. 合并两个有序链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Utils import ListNode, deserialize_linked_list, print_linked_list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            p1 = list1
            p2 = list2
            dummy = ListNode()
            p3 = dummy
            while p1 and p2:
                if p1.val < p2.val:
                    dummy.next = ListNode(p1.val)
                    p1 = p1.next
                else:
                    dummy.next = ListNode(p2.val)
                    p2 = p2.next
                dummy = dummy.next
            if p1:
                dummy.next = p1
            if p2:
                dummy.next = p2
            return p3.next






if __name__ == '__main__':
    s = Solution()
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]

    head = s.mergeTwoLists(deserialize_linked_list(l1), deserialize_linked_list(l2))
    print_linked_list(head)

