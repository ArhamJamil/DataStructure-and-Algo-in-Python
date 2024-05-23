"""
A Binary Search Tree (BST) is a binary tree data structure where each node has at most two child nodes,
    referred to as the left child and the right child. The key property of a BST is that for each node:

        All nodes in the left subtree have values less than the node's value.
        All nodes in the right subtree have values greater than the node's value.

This property makes BSTs suitable for efficient searching, insertion, and deletion operations.

Searching in a BST is typically done by comparing the target value with the current node's value and 
moving left or right accordingly, which allows for a time complexity of O(log n) for balanced trees and O(n) 
for unbalanced trees in the average case.

BSTs are used in many applications, including implementing associative arrays (e.g., map, dictionary) and in database systems for indexing. Maintaining the balance of the tree (ensuring that it remains relatively balanced to maintain the O(log n) complexity) is important to ensure optimal performance.
"""


class TreeNode:
    def __init__(self, val):
        self.value = val
        self.RightPointer = None
        self.LeftPointer = None


class Binary_Search_Tree(TreeNode):
    def __init__(self, val, parent=None):
        super().__init__(val)

    def DFS_PreOrder_Traversal(self):

        print(self.value)

        if self.LeftPointer != None:
            self.LeftPointer.DFS_PreOrder_Traversal()

        if self.RightPointer != None:
            self.RightPointer.DFS_PreOrder_Traversal()

    def DFS_PostOrder_Traversal(self):

        if self.LeftPointer != None:
            self.LeftPointer.DFS_PreOrder_Traversal()

        if self.RightPointer != None:
            self.RightPointer.DFS_PreOrder_Traversal()

        print(self.value)

    def DFS_InOrder_Traversal(self):

        if self.LeftPointer != None:
            self.LeftPointer.DFS_PreOrder_Traversal()

        print(self.value)

        if self.RightPointer != None:
            self.RightPointer.DFS_PreOrder_Traversal()

    def insertValue(self, val):
        if val < self.value:
            if self.LeftPointer == None:
                newTreeNode = Binary_Search_Tree(val, parent=self)
                self.LeftPointer = newTreeNode
            else:
                self.LeftPointer.insertValue(val)

        else:
            if self.RightPointer == None:
                newTreeNode = Binary_Search_Tree(val, parent=self)
                self.RightPointer = newTreeNode
            else:
                self.RightPointer.insertValue(val)


BST = Binary_Search_Tree(10)
dataList = [20, 40, 1, 5, 80, 70, 35, 90, 3, 2, 6, 95]
for i in range(0, len(dataList)):
    BST.insertValue(dataList[i])


print("\nPRE ORDER TRAVERSAL\n")
BST.DFS_PreOrder_Traversal()

print("\nPOST ORDER TRAVERSAL\n")
BST.DFS_PostOrder_Traversal()

print("\nIN ORDER TRAVERSAL\n")
BST.DFS_InOrder_Traversal()
