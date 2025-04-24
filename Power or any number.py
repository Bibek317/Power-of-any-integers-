# power of any numbers
while True:
    try:
        a = float(input("Enter the value of (a): "))
        b = float(input("Enter the power of the number: ")) 
        power_of_a = a**b
        print(f"The power of {a} raised to {b} is: {power_of_a}")  
        another_calculation = input("Do you want to perform one more calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
    except KeyboardInterrupt:
        print("\nProgram was terminated by user.")
        break
