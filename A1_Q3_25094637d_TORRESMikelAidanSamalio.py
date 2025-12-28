## Mikel's work. Again, I swear that no form of generative AI was used. Not even in VS Code for this sentence, on my life.

N = int(input("Enter the number of digits you want in your Fibonacci sequence: "))

fibonacci = [0] 

if N > 1:
    fibonacci.append(1)
    counter = 2 

    while counter < N: 
        next = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next)
        counter += 1 

print(fibonacci)