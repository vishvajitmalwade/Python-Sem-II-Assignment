from Temperature import celsius_to_kelvin
from Temperature import celsius_to_fahrenheit
from Temperature import fahrenheit_to_celsius

def Temperature_main():
    while True:
        print("1. Celcius to Kelvin")
        print("2. Celcius to Fahrenheit")
        print("3. Fahrenheit to Celcius")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            celsius = float(input("Enter temperature in Celcius: "))
            print("Temperature in Kelvin:", celsius_to_kelvin(celsius))

        elif choice == 2:
            celsius = float(input("Enter temperature in Celcius: "))
            print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))

        elif choice == 3:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print("Temperature in Celcius:", fahrenheit_to_celsius(fahrenheit))

        elif choice == 4:
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    Temperature_main()