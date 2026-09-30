n, k = [int(z) for z in input().split()]
# Given: Positive integers n≤40 and k≤5
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
# rabbit pairs (instead of only 1 pair).

arr = [1, 1, k + 1]
print(arr)

for x in range(1, n):
    temp = arr[2]
    arr[2] = arr[0] * k + arr[1]
    arr[0] = arr[1]
    arr[1] = temp
    print(arr)

print(arr[2])
