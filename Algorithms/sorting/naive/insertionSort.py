def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i -1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            arr[j] = key
            j -= 1
    return arr

# Time = O(n^2)
# Space = O(1)


# TEST
assert insertionSort([5, 3, 4, 2, 1]) == [1, 2, 3, 4, 5]
assert insertionSort([98, 56, 87, 45]) == [45, 56, 87, 98]

print("Passed ✔")