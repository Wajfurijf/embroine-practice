arr=list(map(int,input("Enter numbers with space: ").split()))
n=len(arr)

for i in range(n-1):
    for j in range(i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Sorted array is:", sorted(arr))

