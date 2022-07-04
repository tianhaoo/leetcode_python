# 23. 合并K个升序链表
import heapq
from typing import List, Optional
from Utils import ListNode, deserialize_linked_list

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        dummy_head = dummy_tail = ListNode()

        heap = []
        for i, head in enumerate(lists):
            if head:
                # i 是用来防止val相同的时候，head比不了
                heapq.heappush(heap, (head.val, i, head))
        while heap:
            _, i, head = heapq.heappop(heap)
            dummy_tail.next = head
            dummy_tail = dummy_tail.next
            if head.next:
                heapq.heappush(heap, (head.next.val, i, head.next))

        return dummy_head.next



if __name__ == '__main__':
    s = Solution()
    # lists = [[1,4,5],[1,3,4],[2,6]]
    lists = [[]]
    heads = [deserialize_linked_list(lst) for lst in lists]
    print(s.mergeKLists(heads))