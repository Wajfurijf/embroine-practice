a=list(map(int,input("Enter elements of first array: ").split()))
b=list(map(int,input("Enter elements of second array: ").split()))

union=sorted(set(a) | set(b))
print("union:",union)
