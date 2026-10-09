arr=list(map(int,input("Enter 0,1 or 2:").split()))
n=len(arr)
low=0
mid=0
high=n-1

for i in range(n):
    if arr[mid]==0:
        arr[low],arr[mid]=arr[mid],arr[low]
        low += 1
        mid += 1
    elif arr[mid]==1:
        mid += 1
    elif arr[mid]==2:
        arr[mid],arr[high]=arr[high],arr[mid]
        high -= 1
print("Sorted array is:", sorted(arr))
