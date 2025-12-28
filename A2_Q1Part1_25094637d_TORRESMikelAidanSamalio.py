def validate_input(n):
    N = str(n)
    while len(N) < 4:
        N = "0" + N

    if len(N) > 4:
        print("Nope. The number's too long!")
        return False
    
    for i in N:
        if i != N[0]:
            return True

    print("Nope. The number must contain at least two different digits.")
    return False


def sort_digits(n, b):
    N = str(n)
    while len(N) < 4:
        N = "0" + N
    digits = []

    if b:
        for digit in N:
            digits.append(digit)
        
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                if digits[i] < digits[j]:
                    temp = digits[i]
                    digits[i] = digits[j]
                    digits[j] = temp

        descending = ""
        for d in digits:
            descending += d

        return int(descending)
    else:
        for digit in N:
            digits.append(digit)

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                if digits[i] > digits[j]:
                    temp = digits[i]
                    digits[i] = digits[j]
                    digits[j] = temp
        
        ascending = ""
        for d in digits:
            ascending += d
        
        return int(ascending)

def main():
    """
    After running the main function using all the test cases, I can conclude that the
    program will always have a final output of 6174, no matter what. After a Google search,
    I've discovered that this is known as Kaprekar's constant. When you take any four-digit
    number with at least two different digits), take the largest and smallest numbers that
    can be formed from those digits, and subtract the smaller from the larger, you will
    always eventually reach 6174. A curious phenonmenon! I actually didn't know about this,
    but you learn something new everyday.

    Hence, the first and third digits of the final result will always be 6 and 7.
    """

    n = input("Enter a 4-digit number with at least two different digits: ")
    while not validate_input(n):
        n = input("Enter a 4-digit number with at least two different digits: ")
    
    prev_n = ""
    while prev_n != n:
        prev_n = n
        n = str(sort_digits(n, True) - sort_digits(n, False))
        while len(n) < 4:
            n = "0" + n
        print(n)

    print(f"End result: {n}")
    print(f"First digit: {n[0]}, third digit: {n[2]}")

main()