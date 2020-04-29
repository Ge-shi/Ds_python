from list import SingleLinkList

if __name__ == '__main__':
    l2 = SingleLinkList()
    for item in range(1, 10):
        l2.append(item)
    l2.travel()
