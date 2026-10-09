class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# Binary tree banao
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(7, TreeNode(6), TreeNode(9))

s = Solution()
result = s.invertTree(root)


# Tree ko list ki form mein print karo
def printTree(root):
    if root is None:
        return []

    return [root.val] + printTree(root.left) + printTree(root.right)


print(printTree(result))



#using bfs
