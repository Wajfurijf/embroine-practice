arr=list(map(int,input("Enter the array elements: ").split()))
num=int(input("Enter a number: "))
n=len(arr)
def linersearch(arr):
    for i in range(n):
        if arr[i] == num:
            print(f"{num} is present at index {i}")
        else:
            pass
linersearch(arr)
