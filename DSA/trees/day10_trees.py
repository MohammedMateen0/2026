class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def invert_tree(self,root:TreeNode)->TreeNode:
        if not root:
            return None
        root.left,root.right,root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root

    def max_depth(self,root:TreeNode)->int:
        depth=0
        
        if not root:
            return 0
        depth =1+max(self.max_depth(root.left),self.max_depth(root.right))
        return depth
if __name__=="__main__":
    root=TreeNode(4)
    root.left=TreeNode(2)
    root.right=TreeNode(7)
    root.left.left=TreeNode(1)
    root.left.right=TreeNode(3)
    root.right.left=TreeNode(6)
    root.right.right=TreeNode(9)
    solver=Solution()
    print("Max Depth:", solver.max_depth(root))
    inverted=solver.invert_tree(root)
    from collections import deque
    queue=deque([inverted])
    while queue:
        node=queue.popleft()
        print(node.val,end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)



        