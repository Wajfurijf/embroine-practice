
arr=list(map(int,input("Enter numbers with space: ").split()))
n=len(arr)
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if arr[j]<arr[min]:
            min=j
    arr[j],arr[min]=arr[min],arr[j]
print("Sorted array is:", sorted(arr))
