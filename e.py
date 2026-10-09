n=int(input("Enter a number between 1 and 26:"))

if n<1 or n>26:
    print("Invalid input")

else:
    start=ord('A') + n - 1

for i in range(n):
    row_start=start - i
    for ch in range(row_start, start + 1):
        print(chr(ch), end=" ")
    print()