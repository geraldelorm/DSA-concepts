def largest_concat(list):
    result = ""
    while len(list) > 0:
        maxi = max(list)
        result += str(maxi) #O(n)
        list.remove(maxi) #O(n)
    return int(result)

# Time = O(n^2)
# Space = O(1)

# Test
assert concat([2, 1, 5]) == 521
assert concat([2, 8, 5, 1]) == 8521

print("Passed ✔")