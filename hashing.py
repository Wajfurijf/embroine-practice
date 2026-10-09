charecters=input("Enter charceters with space between:")
arr=list(charecters)

frequency = {}
for ch in arr:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
print("Array", arr)
print("Number of times each element appeared:")

for ch,count in frequency.items():
    print(ch,"appeared",count,"time(s)")
