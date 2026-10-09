num1=int(input("Enter any number:"))
num2=int(input("Enter any number:"))

for i in range(1,min(num1,num2)):
    if num1 % i == 0 and num2 % i == 0:
        gcd=i
print(f"The greatest common divisor of {num1} and {num2} is", gcd)

        
