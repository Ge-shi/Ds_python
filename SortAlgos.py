class Sort(object):

    def bubble_sort(self, alist):
        """冒泡排序"""
        length = len(alist)
        for i in range(length - 1):
            for j in range(length - i - 1):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]

    def insert_sort(self, alist):
        """插入排序"""
        length = len(alist)
        for i in range(1, length):
            while i-1 >= 0 and alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1

    def choose_sort(self, alist):
        """选择排序"""
        length = len(alist)
        for i in range(length):
            index = i
            for j in range(i+1, length):
                if alist[j] < alist[index]:
                    index = j
            alist[i], alist[index] = alist[index], alist[i]
