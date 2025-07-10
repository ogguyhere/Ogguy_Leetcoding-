# Leetcode no 104 : Maximum Depth of Binary Tree

# Definition for a binary tree node.

from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0 

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left,right) + 1
    


if __name__ == "__main__":
    # Creating a sample tree: 
    #       1
    #        \
    #         2
    #        /
    #       3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    sol = Solution()
    output = sol.maxDepth(root)
    print("Inorder Traversal:", output)