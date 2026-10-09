n=int(input("Enter number of rows:"))

for i in range(n):
    print(" " * i, end="")
    print("*" * (2*n - (2*i + 1)))