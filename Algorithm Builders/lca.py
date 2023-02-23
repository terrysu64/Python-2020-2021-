#lca on leetcode binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.test = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node: return False
            if node in [p,q]: return node
            resl,resr = dfs(node.left),dfs(node.right)
            if (resl or node==p) and (resr or resr==q): return node
            if (resl or node==q) and (resr and node==p): return node
            return resl or resr
        
        return dfs(root)
