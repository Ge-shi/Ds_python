# st1 = "112"
# st1.replace("1", "9")
# print(st1)
# str2 = "this is string example....wow!!! this is really string"
# str2.replace("is", "was")
# print(str2)
# str2.replace("is", "was", 3)
# print(str2)
# class Solution:


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


list4 = [5, 1, 3, 4, 6, 9, 8, 7]
quick_sort(list4, 0, len(list4) - 1)
print(list4)
