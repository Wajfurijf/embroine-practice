arr=list(map(int,input("Enter the array elements: ").split()))
n=len(arr)
xor1=0
xor2=0

for i in range(n-1):
    xor1=xor1 ^ (i+1)
    xor2=xor2 ^arr[i]
xor1=xor1 ^ (n)
print("The missing element is: ", xor1^xor2)
