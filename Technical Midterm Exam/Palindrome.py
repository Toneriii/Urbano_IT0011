def is_palindrome(number):

    num_str = str(number)
    return num_str == num_str[::-1]


try:
    file = open("numbers.txt", "r")

    lines = file.readlines()
    
    for i, line in enumerate(lines, 1):

        numbers = line.strip().split(",")
        

        total = 0
        for num in numbers:
            total += int(num.strip())
            
        if is_palindrome(total):
            result = "Palindrome"
        else:
            result = "Not a palindrome"
            

        print(f"Line {i}: {line.strip()} (sum {total}) - {result}")
    
    file.close()
    
except FileNotFoundError:
    print("numbers.txt file not found")
except:
    print("An error occurred while processing the file")