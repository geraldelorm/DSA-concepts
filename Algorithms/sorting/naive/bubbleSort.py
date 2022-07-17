def bubbleSort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
    return arr
    
# Time = O(n^2)
# Space = O(1)


# TEST
assert bubbleSort([5, 3, 4, 2, 1]) == [1, 2, 3, 4, 5]
assert bubbleSort([98, 56, 87, 45]) == [45, 56, 87, 98]

print("Passed ✔")