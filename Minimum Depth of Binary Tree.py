class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """

        :type root: TreeNode

        :rtype: int

        """

        if not root:

            return 0

        l = self.minDepth(root.left)

        r = self.minDepth(root.right)

        if not l or not r:

            return 1 + l + r

        return 1 + min(l, r)