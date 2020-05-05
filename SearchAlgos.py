def binary_search(alist, item):
    """非递归"""
    start = 0
    end = len(alist) - 1
    while end >= start:
        mid = (start + end) // 2
        if item == alist[mid]:
            return True
        elif item > alist[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False


def binary_search_re(alist, item):
    if len(alist) == 0:
        return False
    mid = len(alist) // 2
    if alist[mid] == item:
        return True
    elif alist[mid] > item:
        return binary_search_re(alist[mid + 1:], item)
    else:
        return binary_search_re(alist[:mid-1], item)
