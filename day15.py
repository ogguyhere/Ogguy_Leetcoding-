# Leetcode no 94 : Binary Tree Inorder Traversal

# Definition for a binary tree node.
from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def myfunction(self, root:Optional[TreeNode], result: List[int]) -> List[int]:
        if root is None:
            return result 
        
        self.myfunction(root.left, result)
        result.append(root.val)
        self.myfunction(root.right,result)
        return result
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.myfunction(root,result)
        return result
    

        


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
    output = sol.inorderTraversal(root)
    print("Inorder Traversal:", output)