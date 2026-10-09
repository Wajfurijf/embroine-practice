n=int(input("Enter any number:"))

digits=len(str(n))

original=n

sum=0

while True:
    digit=n%10
    n=n//10
    sum=sum + (digit**digits)
    if original==sum:
        print(f"{original} is an armstrong number")
    else:
        print(f"{original} is not an armstrong number")
    break


        
