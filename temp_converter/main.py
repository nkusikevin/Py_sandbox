def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit



def main():
    print("Select an option:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

    choice = int(input("Enter your choice (1-2): "))

    if choice == 1:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
