class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data),
        inOrder(root.right)


def preOrder(root):
    if root:
        print(root.data),
        preOrder(root.left)
        preOrder(root.right)


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data),


if __name__ == '__main__':
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)

    print("Inorder is ")
    inOrder(tree)
    print("Preorder is ")
    preOrder(tree)
    print("Postorder is ")
    postOrder(tree)
