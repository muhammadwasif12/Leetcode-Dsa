class Solution:
    def isSubtree(self, root, subRoot):

        def sameTree(root1, root2):
            if root1 is None and root2 is None:
                return True

            if root1 is None or root2 is None:
                return False

            if root1.val != root2.val:
                return False

            return sameTree(root1.left, root2.left) and sameTree(
                root1.right, root2.right
            )

        if root is None:
            return False

        if sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
