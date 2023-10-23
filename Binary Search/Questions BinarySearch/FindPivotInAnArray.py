"""
Question: Find Pivot in an array using binary search

e.g : [7,9,1,2,3] 
pivot = 1 (minimum)


Finding a pivot in an array using binary search can be a bit tricky, 
as it requires a specific scenario where the pivot is present. The binary search 
approach assumes that you have a sorted array that has been rotated at some pivot point.

"""
def find_pivot(arr):
    StartIndex = 0
    EndIndex = len(arr) - 1

    while StartIndex < EndIndex:
        mid = int((StartIndex + EndIndex) / 2)

        # If the element at mid is greater than the element at the right,
        # it means the pivot is to the right of mid.
        if arr[mid] > arr[EndIndex]:
            StartIndex = mid + 1
        # If the element at mid is less than or equal to the element at the right,
        # it means the pivot is to the left of or equal to mid.
        else:
            EndIndex = mid

    # The left index now points to the pivot element.
    return StartIndex

# Example usage:
arr = [3,8,10,17,1]
pivot_index = find_pivot(arr)
pivot_value = arr[pivot_index]
print(f"The pivot is at index {pivot_index} with value {pivot_value}")
