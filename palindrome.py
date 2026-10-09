user_input=input("Enter any word:")

while True:
    if user_input==user_input[::-1]:
        print(user_input,"is a palindrome")
        break
    else:
        print(f"{user_input} is not a palindrome")
        break