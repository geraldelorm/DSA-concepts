def change(money, denominations = [10, 5, 1]):
    numOfCoins = 0
    while money > 0:
        if money >= 10:
            money = money - 10
        elif money >= 5:
            money = money - 5
        else:
            money = money - 1
        numOfCoins += 1

    return numOfCoins



# Time = O(n)
# Space = O(1)

# Test
assert change(20) == 2
assert change(23) == 5
assert change(25) == 3

print("Passed ✔")