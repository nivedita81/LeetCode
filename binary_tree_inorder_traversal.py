from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #result = []
        if root is None:
            return []
        if root:
            if root.left:
                self.inorderTraversal(root.left)
            result.append(root.val)
            if root.right:
                self.inorderTraversal(root.right)

        return result


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    # res = []
    res = Solution().inorderTraversal(tree)
    print(res)

