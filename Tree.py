class TreeNode:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.__root = None

    def add(self, item):
        node = TreeNode(item)
        if self.__root is None:
            self.__root = node
        else:
            queue = list()
            queue.append(self.__root)
            while queue:
                cur = queue.pop()
                if cur.left is None:
                    cur.left = node
                    return
                if cur.right is None:
                    cur.right = node
                    return
                queue.append(cur.left)
                queue.append(cur.right)

    def preorder(self, root: TreeNode):
        if root is None:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root: TreeNode):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def postorder(self, root: TreeNode):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)

    def breadth_travel(self, root: TreeNode):
        if root is None:
            return
        queue = list()
        queue.append(root)
        while queue:
            cur = queue.pop(0)
            print(cur.val)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
