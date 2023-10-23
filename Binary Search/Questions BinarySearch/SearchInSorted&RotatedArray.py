
def find_pivot(arr):
    StartIndex = 0
    EndIndex = len(arr) - 1
    while StartIndex < EndIndex:
        mid = int((StartIndex + EndIndex) / 2)
        if arr[mid] > arr[EndIndex]:
            StartIndex = mid + 1
        else:
            EndIndex = mid
    return StartIndex

def BinarySearch(key, arr , starting, ending):
    startIndex = starting
    endIndex = ending 
    while (startIndex <= endIndex):
        x = (startIndex + endIndex) / 2
        mid = int(x)
        if arr[mid] == key:
            return arr[mid]
        if key > arr[mid]:
            startIndex = mid + 1
        else:
            endIndex = mid - 1

    return -1

def SearchInRotatedAndSortedArray(arr, target):
    pivotValue = find_pivot(arr)

    if target >= arr[pivotValue] and target <= arr[len(arr) - 1]:
        return BinarySearch(target, arr, pivotValue, len(arr) - 1)
    else:
        return BinarySearch(target, arr, 0, pivotValue - 1)

arr = [3,8,10,17,1]
isFound = SearchInRotatedAndSortedArray(arr, 8)
print(isFound)



"""
# BreakDown of Code : 

  * The find_pivot function finds the pivot index by repeatedly updating the StartIndex 
    and EndIndex based on whether the middle element (arr[mid]) is greater than the last 
    element (arr[EndIndex]). The pivot index is the index of the first element in the 
    descending part of the array.

  * The BinarySearch function performs a standard binary search in a given range of the array. 
    It calculates the mid index and compares the key with arr[mid] to determine whether to search 
    in the left or right half of the range.

  * In the SearchInRotatedAndSortedArray function, the pivot index is first found using 
    find_pivot. Then, it checks whether the target is within the range [pivotValue, pivotValue],
    which is not a valid condition. Instead, it should check whether the target is greater than
    or equal to arr[pivotValue] and less than or equal to arr[len(arr) - 1]. If this condition 
    is met, it calls BinarySearch to search in the right half of the array; otherwise, 
    it searches in the left half.

  * Finally, the code searches for the target element in the provided rotated and 
    sorted array arr and returns the result.

"""