arr=list(map(int,input("Enter numbers with space: ").split()))
k=int(input("Enter any number: "))
n=len(arr)

left=0
right=0
sum=arr[0]
maxlen=0
start_index= -1
    
for right in range(n):
    sum += arr[right]
    right += 1

    while sum > k:
        sum -= arr[left]
        left += 1

    if sum == k:
        if right - left + 1 > maxlen:
            maxlen=right - left + 1
            start_index=left
print(maxlen)
if maxlen > 0:
    print("Longest subarray is", arr[start_index:start_index + maxlen])
else:
    print("No subarray with sum",k)



