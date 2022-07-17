def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


# Time = O(n^2)
# Space = O(1)


# TEST
assert selectionSort([5, 3, 4, 2, 1]) == [1, 2, 3, 4, 5]
assert selectionSort([98, 56, 87, 45]) == [45, 56, 87, 98]

print("Passed ✔")