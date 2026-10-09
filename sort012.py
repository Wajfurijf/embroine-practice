arr=list(map(int,input("Enter 0,1 or 2:").split()))
zero=[x for x in arr if x==0]
one=[x for x in arr if x==1]
two=[x for x in arr if x==2]

arr=zero + one + two
print("Sorted array is: ", arr)

