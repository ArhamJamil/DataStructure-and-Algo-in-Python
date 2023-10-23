def Reverse(arr, size):
    startPointer = 0
    endPointer = size - 1

    while (startPointer <= endPointer):
        Temp = arr[startPointer]
        arr[startPointer] = arr[endPointer]
        arr[endPointer] = Temp

        startPointer = startPointer + 1
        endPointer = endPointer - 1
    

my_array = [10,12,13,6,7,8,9,20,22]
print("Actual Order: ",my_array)
Reverse(my_array, len(my_array))
print("Reverse Order: ",my_array)