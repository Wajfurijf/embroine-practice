arr=list(map(int,input("Enter numbers with space in between: ").split()))
is_sorted=True

for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
        is_sorted=False
        break

if is_sorted:
    print("Array is sorted")
else:
    print("Not sorted")


    

