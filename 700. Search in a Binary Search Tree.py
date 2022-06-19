class Solution:
    '''
    700. Search in a Binary Search Tree: https://leetcode.com/problems/search-in-a-binary-search-tree/
    '''
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while(root and root.val != val):
            if(val < root.val):
                root = root.left
            else:
                root = root.right
        return root