# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
#从贡献的角度来说 比较好说

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # 2. 递归计算左右子树的最大贡献（负数直接舍弃，选0）
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # 3. 计算：当前节点作为顶点的【分叉路径和】，更新全局最大值
            current_path = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path)
            
            # 4. 向上返回：单链最大值（只能选左 or 右）
            return node.val + max(left_gain, right_gain)
        
        # 执行递归
        dfs(root)
        # 返回全局最大路径和
        return self.max_sum