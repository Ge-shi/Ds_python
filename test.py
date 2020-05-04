from list import SingleLinkList
from cyclist import cycSingleLinklist
import SortAlgos
import SearchAlgos


if __name__ == '__main__':
    l2 = SingleLinkList()
    for item in range(1, 10):
        l2.append(item)
    l2.travel()
    l2.insert(4, 10)
    l2.travel()
    l2.add(0)
    l2.travel()
    l2.search(10)
    l2.remove(10)
    l2.travel()
    print("单循环链表", end='\n')
    l1 = cycSingleLinklist()
    for i in range(1, 10):
        l1.append(i)
    l1.travel()
    l1.remove(9)
    l1.travel()
    l1.remove(1)
    print(l1.search(4))
    l1.travel()
    list1 = [1, 2, 3, 4, 6, 5, 9, 7, 8, 0, -1, 100, -34]
    SortAlgos.choose_sort(list1)
    print(list1)
    list2 = [1, 2, 3, 4, 6, 5, 9, 7, 8, 0, -1, 100, -34]
    SortAlgos.bubble_sort(list2)
    print(list2)
    list3 = [1, 2, 3, 4, 6, 5, 9, 7, 8, 0, -1, 100, -34]
    SortAlgos.bubble_sort(list3)
    print(list3)
    list4 = [5, 1, 3, 4, 6, 9, 8, 7]
    SortAlgos.quick_sort(list4, 0, len(list4) - 1)
    print(list4)
    list5 = [5, 1, 3, 4, 6, 9, 8, 7]
    SortAlgos.shell_sort(list5)
    print("list5   ", list5)
    seq = [5, 3, 0, 6, 1, 4]
    print('排序前：', seq)
    result = SortAlgos.mergesort(seq)
    print('排序后：', result)
    print(SearchAlgos.binary_search(seq, 4))
    print(SearchAlgos.binary_search(seq, 100))
    print(SearchAlgos.binary_search_re(seq, 4))
    print(SearchAlgos.binary_search_re(seq, 100))
