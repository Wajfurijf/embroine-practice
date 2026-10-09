arr=list(map(int,input("Enter numbers with space in between: ").split()))
n=len(arr)

largest = arr[0]
for i in range(n):
    if arr[i] > largest:
        largest = arr[i]
print("Largest is: ", largest)


