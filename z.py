import random
while True:
    try:
        command=input("Roll the dice?(y/n):")
        if command != 'y' and command != 'n':
            pass
            
        elif command=='y':
            x=random.randint(1,6)
            y=random.randint(1,6)
            print(f'{x},{y}')
            break
        else:
            print("Thank You!")
        break
    except ValueError:
        print("Invalid input")


