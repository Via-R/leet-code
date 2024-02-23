# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            left_list = dfs(node.left) if node.left else []
            right_list = dfs(node.right) if node.right else []
            left_list.append(node.val)
            left_list.extend(right_list)

            return left_list

        first_list, second_list = dfs(root1), dfs(root2)

        result = []
        while len(first_list) and len(second_list):
            if first_list[0] <= second_list[0]:
                result.append(first_list.pop(0))
            else:
                result.append(second_list.pop(0))

        if len(first_list):
            result.extend(first_list)
        else:
            result.extend(second_list)

        return result