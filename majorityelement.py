arr=list(map(int,input("Enter the array elements: ").split()))
n=len(arr)

count=0
element=arr[0]

for i in range(n):
    if count==0:
            count=1
            element=arr[i]
    elif arr[i]==element:
        count+=1
    else:
        count -= 1
print(f"{arr[i]} element is appearing {count} times")
count1=0
for i in range(n):
    if arr[i] == element:
        count1 += 1
    if count1 > n//2:
        print(f"Majority element {element} occurs {count1} times")


