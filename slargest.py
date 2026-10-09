arr=list(map(int,input("Enter numbers with space in between: ").split()))
n=len(arr)

largest = arr[0]
slargest = min(arr)

for i in range(n):
    if arr[i] > largest:
        largest = arr[i]
for i in range(n):
    if arr[i] < largest and arr[i] > slargest:
        slargest = arr[i]
print("Second largest element of the array is: ", slargest)


