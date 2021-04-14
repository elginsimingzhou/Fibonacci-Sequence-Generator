#Fibonacci Sequence
#Each number is the sum of the two preceding ones, starting from 0 and 1.
#Enter a number and the program will generate the Fibonacci sequence to Nth number

def recur_fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return recur_fib(n-1) + recur_fib(n-2)


N = int(input("Please enter a integer"))

fib_seq = []

if N <= 0:
    print("Sorry, please enter a positive integer: ")
else:
    for i in range(1, N + 1):
        fib_seq.append(recur_fib(i))
    print(fib_seq)
