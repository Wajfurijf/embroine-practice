n=int(input("Enter the number of rows:"))

for i in range(n):
    print("*" * (n - i) + " " * 2*i + "*" * ( n - i))
for i in range(2, n + 1):
    print("*" * i + " " * (2*(n - i)) + "*" * i)
