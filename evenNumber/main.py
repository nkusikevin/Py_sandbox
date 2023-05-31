def check_odd_even(number):
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")

def main():
    number = int(input("Enter a number: "))
    check_odd_even(number)

if __name__ == "__main__":
    main()
