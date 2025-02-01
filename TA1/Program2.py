def sum_digits(str):
    total = 0

    for char in str:
        if char >= "0" and char <= "9":
            total += int(char)

    print("Sum of digits:", total)

str = input("Enter a string with digits: ")
sum_digits(str)
