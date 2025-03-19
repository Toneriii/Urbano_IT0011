def divide(a, b):
    if b == 0:
        return None
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        return None
    return a % b

def summation(start, end):
    if start > end:
        return None
    return sum(range(start, end + 1))

def main():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").upper()
        
        if choice == 'Q':
            print("Exiting program.")
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                
                if choice == 'D':
                    result = divide(num1, num2)
                elif choice == 'E':
                    result = exponentiation(num1, num2)
                elif choice == 'R':
                    result = remainder(num1, num2)
                elif choice == 'F':
                    result = summation(num1, num2)
                
                print(f"Result: {result}") if result is not None else print("Invalid input.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
