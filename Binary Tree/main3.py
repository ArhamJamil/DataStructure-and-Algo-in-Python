# Initialize BST list with -1 for left and right pointers and 0 for data
BST_list = [[-1, 0, -1] for _ in range(15)]

# Helper function to find the next available index in BST_list
def getNextAvailableIndex():
    for i in range(len(BST_list)):
        if BST_list[i][1] == 0:
            return i
    return -1

# Function to add data to the BST
def addData(data, root):
    if BST_list[root][1] == 0:
        BST_list[root][1] = data
    else:
        if data < BST_list[root][1]:
            if BST_list[root][0] == -1:
                nextIndex = getNextAvailableIndex()
                if nextIndex != -1:
                    BST_list[root][0] = nextIndex
                    BST_list[nextIndex][1] = data
                else:
                    print("No space available to insert new data.")
            else:
                addData(data, BST_list[root][0])
        else:
            if BST_list[root][2] == -1:
                nextIndex = getNextAvailableIndex()
                if nextIndex != -1:
                    BST_list[root][2] = nextIndex
                    BST_list[nextIndex][1] = data
                else:
                    print("No space available to insert new data.")
            else:
                addData(data, BST_list[root][2])


def InOrder_traversal(root):
    if BST_list[root][0] != -1:
        InOrder_traversal(BST_list[root][0])
    
    print(BST_list[root][1])

    if BST_list[root][2] != -1:
        InOrder_traversal(BST_list[root][2])

def PostOrder_traversal(root):
    if BST_list[root][0] != -1:
        PostOrder_traversal(BST_list[root][0])

    if BST_list[root][2] != -1:
        PostOrder_traversal(BST_list[root][2])
    
    print(BST_list[root][1])


def PreOrder_traversal(root):  
    print(BST_list[root][1])
    
    if BST_list[root][0] != -1:
        PreOrder_traversal(BST_list[root][0])

    if BST_list[root][2] != -1:
        PreOrder_traversal(BST_list[root][2])
  




# Add data to BST
addData(10, 0)
addData(8, 0)
addData(12, 0)
addData(5, 0)
addData(9, 0)
addData(11, 0)
addData(14, 0)

print("POST ORDER: ")
PostOrder_traversal(0)

print("IN ORDER: ")
InOrder_traversal(0)

print("PRE ORDER: ")
PreOrder_traversal(0)

