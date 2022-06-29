import math

import Utils


def merge(left_lst, right_lst):
    """将两个有序数组合并，返回合并后的数组"""
    left_index, right_index = 0, 0
    res = []
    while left_index < len(left_lst) and right_index < len(right_lst):
        left_elem = left_lst[left_index]
        right_elem = right_lst[right_index]
        if left_elem < right_elem:
            res.append(left_elem)
            left_index += 1
        else:
            res.append(right_elem)
            right_index += 1
    # 将剩余元素添加到末尾
    if left_index < len(left_lst):
        res.extend(left_lst[left_index:])
    if right_index < len(right_lst):
         res.extend(right_lst[right_index:])
    return res


@Utils.trace
def merge_sort(lst):
    if len(lst) >= 2:
        mid = math.floor(len(lst)/2)
        lst1 = merge_sort(lst[:mid])
        lst2 = merge_sort(lst[mid:])
        res = merge(lst1, lst2)
        return res
    else:
        return lst




if __name__ == '__main__':
    lst = [9, 6, 1, 3, 15, 4, 7, 10, 12, 8]

    print(merge_sort(lst))
