arr=list(map(int,input("Enter numbers with a space: ").split()))
n=len(arr)

for i in range(n-1):
    j=i
    while(j>0 and arr[j-1]>arr[j]):
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j -= 1
print("Sorted array is:", sorted(arr))
