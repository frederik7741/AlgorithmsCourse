def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = bubbleSort(arr)
print("Sorted array:", sorted_arr)
