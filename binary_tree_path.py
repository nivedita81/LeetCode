class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        tree_path = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)]
        tree_path += [str(root.val) + '->' + path for path in self.binaryTreePaths(root.right)]
        return tree_path


if __name__ == '__main__':
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.right = Node(5)
    # res = []
    res = Solution().binaryTreePaths(tree)
    print(res)
