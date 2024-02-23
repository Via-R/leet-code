# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def bfs(nodes):
            next_nodes = []
            val_sum = 0
            for n in nodes:
                if n.left:
                    next_nodes.append(n.left)
                if n.right:
                    next_nodes.append(n.right)
                if not n.left and not n.right:
                    val_sum += n.val

            if not len(next_nodes):
                return val_sum

            return bfs(next_nodes)
