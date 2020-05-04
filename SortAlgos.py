def bubble_sort(alist):
    """冒泡排序"""
    length = len(alist)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]


def insert_sort(alist):
    """插入排序"""
    length = len(alist)
    for i in range(1, length):
        while i-1 >= 0 and alist[i] < alist[i-1]:
            alist[i], alist[i-1] = alist[i-1], alist[i]
            i -= 1


def choose_sort(alist):
    """选择排序"""
    length = len(alist)
    for i in range(length):
        index = i
        for j in range(i+1, length):
            if alist[j] < alist[index]:
                index = j
        alist[i], alist[index] = alist[index], alist[i]


def quick_sort(alist, begin, end):
    if end <= begin:
        return
    temp = alist[begin]
    left = begin
    right = end
    while right > left:
        while right > left and alist[right] >= temp:
            right -= 1
        while right > left and alist[left] <= temp:
            left += 1
        alist[left], alist[right] = alist[right], alist[left]
    alist[begin] = alist[left]
    alist[left] = temp
    quick_sort(alist, begin, left - 1)
    quick_sort(alist, left + 1, end)


def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for i in range(gap, n):
            j = i
            while j - gap >= 0 and alist[j] < alist[j - gap]:
                alist[j], alist[j - gap] = alist[j - gap], alist[j]
                j -= 1
        gap = gap // 2


# def merge_sort(alist):
#     tmp = [] * len(alist)
#     mergesort(alist, 0, len(alist)-1, tmp)


# def mergesort(alist, left, right, temp):
#     if left < right:
#         mid = (left + right) // 2
#         mergesort(alist, left, mid, temp)
#         mergesort(alist, mid + 1, right, temp)
#         merge(alist, left, mid, right, temp)


# def merge(alist1, left1, mid1, right1, temp1):
#     i = left1
#     j = mid1 + 1
#     t = 0
#     while i <= mid1 and j <= right1:
#         if alist1[i] <= alist1[j]:
#             temp1[t] = alist1[i]
#             i += 1
#         else:
#             temp1[t] = alist1[j]
#             j += 1
#         t += 1
#     while i <= mid1:
#         temp1[t] = alist1[i]
#         i += 1
#         t += 1
#     while j <= right1:
#         temp1[t] = alist1[j]
#         j += 1
#         t += 1
#     t = 0
#     while left1 <= right1:
#         alist1[left1] = temp1[t]
#         left1 += 1
#         t += 1
def mergesort(seq):
    """归并排序"""
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)


def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
