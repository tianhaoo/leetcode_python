# 83. 删除排序链表中的重复元素
from Utils import ListNode, deserialize_linked_list


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        slow = fast = head
        while fast:
            if fast.val != slow.val:
                slow = slow.next
                slow.val = fast.val
            fast = fast.next
        slow.next = None
        return head

if __name__ == '__main__':
    s = Solution()
    lst = [1,1,2,3,3]
    head = deserialize_linked_list(lst)
    print(head)
    print(s.deleteDuplicates(head))