arr=list(map(int,input("Enter the array elements: ").split()))
non_zero=[x for x in arr if x != 0]
zero=[x for x in arr if x == 0]
result=non_zero+zero
print(result)