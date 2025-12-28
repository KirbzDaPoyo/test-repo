## Mikel's work. I swear that no form of generative AI was used. Not even in VS Code for this sentence, on my life.

number = int(input("Enter a number to convert: "))

def convert_to_binary(number):
    binary = []
    x = number
    
    if x == 0:
        binary.append(x)
    
    while x > 0:
        digit = int(x % 2)
        binary.insert(0, digit)
        x = (x - digit) // 2
    
    final_binary = ""
    for digit in binary:
        final_binary += str(digit)
    
    return final_binary

def convert_to_hex(number):
    hexadecimal = []
    x = number
    hex_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    
    if x == 0:
        hexadecimal.append(x)
    
    while x > 0:
        i = int(x % 16)
        digit = hex_digits[i]
        hexadecimal.insert(0, digit)
        x = (x - i) // 16

    final_hex = ""
    for digit in hexadecimal:
        final_hex += str(digit)
    
    return final_hex

## Verification functions (they take the strings as input automatically please dont change that)

def verify_binary(binary_string):
    decimal = 0
    
    for i in range(len(binary_string)):
        digit = int(binary_string[len(binary_string) - 1 - i])
        decimal += digit * (2 ** i)
    
    return decimal

def verify_hex(hex_string):
    decimal = 0
    hex_digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    for i in range(len(hex_string)):
        digit = hex_digits[hex_string[len(hex_string) - 1 - i]]
        decimal += digit * (16 ** i)
    
    return decimal

print(convert_to_binary(number))
print(convert_to_hex(number))
print(verify_binary(convert_to_binary(number)))
print(verify_hex(convert_to_hex(number)))