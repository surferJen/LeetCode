class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest_path = 0
        self.longestUniPathHelper(root)
        return self.longest_path
    
    def longestUniPathHelper(self, root):
        if not root:
            return 0
        left_path = self.longestUniPathHelper(root.left)