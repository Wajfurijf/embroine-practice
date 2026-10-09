n=int(input("Enter any number:"))

for i in range(1,n):
    if n % i==0:
        print(f"{i} is a divisor of {n}")
   