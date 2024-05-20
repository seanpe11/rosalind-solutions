n, k = [int(z) for z in input().split()]
### 1, 1, 

arr = [1, 1, k+1]
print(arr)
for x in range(1,n):
    temp = arr[2]
    arr[2] = arr[0] * k + arr[1]
    arr[0] = arr[1]
    arr[1] = temp
    print(arr)

print(arr[2])



