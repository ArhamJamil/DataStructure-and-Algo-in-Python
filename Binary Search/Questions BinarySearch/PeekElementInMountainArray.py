'''
# You are given an MOUNTAIN Array which follows :
    * PEEK ELEMENT > [PEEK ELEMENT + 1] element
    * PEEK ELEMENT < [PEEK ELEMENT - 1] element 
  Find The Peek Element using Binary Search Algorithm

  [0,1,0,-1,-2]
  [0,]

'''
# APPROACH 1

def FindPeekElement(arr):
    StartIndex = 0
    EndIndex = len(arr) - 1

    while StartIndex <  EndIndex :
        x = (StartIndex + EndIndex) / 2
        Mid = int(x)

        if Mid == 0 or (arr[Mid] > arr[Mid - 1] and arr[Mid] > arr[Mid + 1]):
            peekElement = Mid
            StartIndex = Mid + 1

        if arr[Mid] > arr[Mid+1] and arr[Mid] < arr[Mid-1]:
            EndIndex = Mid

        if arr[Mid] < arr[Mid+1] and arr[Mid] > arr[Mid-1]:
            StartIndex = Mid

    return peekElement


# APPROACH 2 

def FindPeakElementIndex(arr):
    StartIndex = 0
    EndIndex = len(arr) - 1

    while StartIndex < EndIndex :
        mid = int((StartIndex+ EndIndex)/2)
        if arr[mid] < arr[mid+1]:
            StartIndex = mid + 1
        else:
            EndIndex = mid

    return StartIndex


        

myList = [0,1,0]
# answer = FindPeekElement(myList)
input_arr = [1,2,1,3,5,6,4]
print(FindPeakElementIndex(input_arr))



