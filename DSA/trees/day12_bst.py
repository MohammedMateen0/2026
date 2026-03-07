class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def is_valid_bst(self,root:TreeNode)->bool:
        def validate(node,low,high):
            if node is None:
                return False
            elif node.val<=low or node.val>=high:
                return False
            validate(node.left,low,node.val)
            validate(node.right,node.val,high)
            return validate(node.left,low,node.val) and \
                validate(node.right,node.val,high)
        return validate(root,-float("inf"),float("inf"))
    def lowest_common_ancestor(self,root:TreeNode,p:TreeNode,q:TreeNode)->TreeNode:
        while root:
            if p.val<root.val and q.val<root.val:
                root=root.left
            elif p.val>root.val and q.val>root.val:
                root=root.right
            else:
                return root
if __name__=="__main__":
    root=TreeNode(6)
    root.left=TreeNode(2)
    root.right=TreeNode(8)
    root.left.left=TreeNode(0)
    root.left.right=TreeNode(4)
    root.left.right.left=TreeNode(3)
    root.left.right.right=TreeNode(5)
    solver=Solution()
    print("Is Vlaid BST: ",solver.is_valid_bst(root))
    p=root.left.right.left
    q=root.left.right.right
    lca =solver.lowest_common_ancestor(root,p,q)
    print("LCA:",lca.val)
        