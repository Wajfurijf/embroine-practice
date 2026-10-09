n=int(input("Enter the number of rows:"))

for i in range(1,n+1):
    print(" " * (n - i) * 2, end=" ")
    for j in range(i):
        print(chr(65 + j), end=" ")
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end=" ")
    print()
    