
# Program to reverse a number and remove zeros from the reversed number

num = int(input("Enter a number: "))

reverse = 0
while num > 0:
    digit= num % 10
    if digit != 0:
        reverse=reverse * 10 + digit
    num //= 10
print("The reversed number is:", reverse)


