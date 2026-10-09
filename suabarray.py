arr = list(map(int,input("Enter the array elements:").split()))
n = len(arr)
k = int(input("Enter the sum u want to to find"))
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == k:
            count += 1
print(count)

