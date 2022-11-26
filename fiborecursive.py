def fib(n):
    if n==0: #base class
        return 0
    elif n==1: #base class
        return 1 
    else:
        return fib(n-1) + fib(n-2)  #recursive fibonacci function call
nterms = int(input("How many terms?"))
if nterms<=0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequences:")
    for i in range(nterms): 
        print(fib(i))
