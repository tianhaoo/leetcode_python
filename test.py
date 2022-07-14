import heapq
import queue

lst = [1,2, 9, 9, 4, 8,7,9]

heapq.heapify(lst)
print(lst)

print(heapq.nlargest(3, lst))


q = queue.PriorityQueue()

print(2**1000)
print(sum(map(int, str(2**1000))))