def convert_temperature():
    print("Temperature Conversion Program")
    print("Select the original unit of measurement:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    choice = int(input("Enter your choice (1/2/3): "))
    temp = float(input("Enter the temperature: "))
    if choice == 1:
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        print(f"{temp} Celsius = {fahrenheit} Fahrenheit")
        print(f"{temp} Celsius = {kelvin} Kelvin")
    elif choice == 2:
        celsius = (temp - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{temp} Fahrenheit = {celsius} Celsius")
        print(f"{temp} Fahrenheit = {kelvin} Kelvin")
    elif choice == 3:
        celsius = temp - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{temp} Kelvin = {celsius} Celsius")
        print(f"{temp} Kelvin = {fahrenheit} Fahrenheit")
    
    else:
        print("Invalid choice! Please select a valid unit (1/2/3).")
convert_temperature()
