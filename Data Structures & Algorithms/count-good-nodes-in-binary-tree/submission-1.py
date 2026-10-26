# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = [0]

        def dfs(root, checker):
            if not root:
                return

            if root.val >= checker:
                good_nodes[0] += 1

            dfs(root.left, max(root.val, checker))
            dfs(root.right, max(root.val,checker))

        dfs(root, root.val)
        return good_nodes[0]
                    