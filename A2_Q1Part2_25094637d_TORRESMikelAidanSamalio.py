def validate_input(n):
    N = str(n)
    while len(N) < 4:
        N = "0" + N

    if len(N) > 4:
        return False
    
    not_two = True
    for i in N:
        if i != N[0]:
            not_two = False

    if not_two:
        return False
    
    return True

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

def run_iters(n):
    prev_n = ""
    counter = 0

    while prev_n != n:
        prev_n = n
        n = str(sort_digits(n, True) - sort_digits(n, False))

        while len(n) < 4:
            n = "0" + n

        counter += 1
    
    return counter

max_iters = 0
max_num = 0
for n in range(1, 9999):
    if validate_input(n):
        N = str(n)
        while len(N) < 4:
            N = "0" + N
        
        steps = run_iters(N)

        if steps > max_iters:
            max_iters = steps
            max_num = N

print("Maximum iterations:", max_iters)
print(max_num)