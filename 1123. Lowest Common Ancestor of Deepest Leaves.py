# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # LCA Solution
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        while queue:
            deepest = []
            for _ in range(len(queue)):
                node = queue.popleft()
                deepest.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        def lca(root):
            if not root:
                return None
            if root.val == deepest[0].val or root.val == deepest[-1].val:
                return root
            left, right = lca(root.left), lca(root.right)
            if left and right:
                return root
            return left or right
        return lca(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # DFS solution
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, depth):
            if not node:
                return (None, depth + 1)

                left_node, left_depth = dfs(node.left, depth + 1)
                right_node, right_depth = dfs(node.right, depth + 1)

                if left_depth > right_depth:
                    return left_node, left_depth
                elif right_depth > left_depth:
                    return right_node, right_depth

                return node, left_depth

        node, _ = dfs(root, 0)
        return node
        
        
