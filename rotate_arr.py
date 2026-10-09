arr = list(map(int, input("Enter the array elements: ").split()))
d=int(input("Enter the number of rotations: "))
d=d%len(arr)
arr = arr[-d:] + arr[:-d]

print("Array after left rotation:", arr)