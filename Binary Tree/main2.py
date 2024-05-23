global ArrayNodes
global FreeNode
global RootPointer

ArrayNodes = [[-1,-1,-1] for _ in range(20)]

FreeNode = 6
RootPointer = 0


ArrayNodes[0][0] = 1
ArrayNodes[0][1] = 20
ArrayNodes[0][2] = 5

ArrayNodes[1][0] = 2
ArrayNodes[1][1] = 15
ArrayNodes[1][2] = -1

ArrayNodes[2][0] = -1
ArrayNodes[2][1] = 3
ArrayNodes[2][2] = 3

ArrayNodes[3][0] = -1
ArrayNodes[3][1] = 9
ArrayNodes[3][2] = 4

ArrayNodes[4][0] = -1
ArrayNodes[4][1] = 10
ArrayNodes[4][2] = -1

ArrayNodes[5][0] = -1
ArrayNodes[5][1] = 58
ArrayNodes[5][2] = -1

ArrayNodes[6][0] = -1
ArrayNodes[6][1] = -1
ArrayNodes[6][2] = -1

print(ArrayNodes)

def SearchValue(Root, ValueToFind):
    global ArrayNodes
    if Root == -1:
        return -1
    else:
        if ArrayNodes[Root][1] == ValueToFind:
            return Root
        else:
            if ArrayNodes[Root][1] == -1:
                return -1
            
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)
    
    if ArrayNodes[Root][0] < ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    

def PostOrder(Root):

    if ArrayNodes[Root][0] != -1:
        PostOrder(ArrayNodes[Root][0])

    if ArrayNodes[Root][2] != -1:
        PostOrder(ArrayNodes[Root][2])

    print(ArrayNodes[Root][1])


def PreOrder(Root):

    print(ArrayNodes[Root][1])

    if ArrayNodes[Root][0] != -1:
        PostOrder(ArrayNodes[Root][0])

    if ArrayNodes[Root][2] != -1:
        PostOrder(ArrayNodes[Root][2])



def INOrder(Root):

    if ArrayNodes[Root][0] != -1:
        PostOrder(ArrayNodes[Root][0])

    print(ArrayNodes[Root][1])

    if ArrayNodes[Root][2] != -1:
        PostOrder(ArrayNodes[Root][2])





searchResult = SearchValue(RootPointer, 15)
if searchResult == -1:
    print("Index not found")
else:
    print("Index: ", searchResult)

print("Post Order:\n")
PostOrder(RootPointer)

print("Pre Order:\n")
PreOrder(RootPointer)

print("In Order:\n")
INOrder(RootPointer)
