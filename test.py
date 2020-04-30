from list import SingleLinkList
from cyclist import cycSingleLinklist

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
