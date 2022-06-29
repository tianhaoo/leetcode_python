import Utils


def partition(lst, start, end):
    """将lst[start:end+1]的数据分成左小右大，并返回分割点的下标"""
    pivot = lst[end]
    i = start-1
    for j in range(start, end):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    # 将pivot放在中间
    i += 1
    lst[i], lst[end] = lst[end], lst[i]
    return i

@Utils.trace
def quick_sort(lst, start, end):
    """将lst升序排列"""
    if start < end:
        i = partition(lst, start, end)
        quick_sort(lst, start, i-1)
        quick_sort(lst, i+1, end)
        return i


if __name__ == '__main__':
    lst = [9, 6, 1, 3, 15, 4, 7, 10, 12, 8]
    print(lst)
    quick_sort(lst, 0, len(lst)-1)

    print(lst)