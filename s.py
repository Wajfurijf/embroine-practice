def main():
    n=int(input("Enter any number:"))
    get_star(n)
def get_star(size):
    for i in range(size):
        print("*"*i)
main()
