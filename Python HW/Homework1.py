#Please write a program that prints the first N prime numbers.
#N should be declared as a variable at the beginning of your code
# or provided as input from the user.

from math import *
N=int(input("Enter a number: "))
count=0
n=2 #the first prime number
print("The first", N, "prime numbers are: ")

#Find the first N prime numbers from 2
while count < N:
    #Check whether n is prime number or not?
    check_prime = True
    for i in range(2, int(sqrt(n)) + 1):
    #if n is divisible by i (i is from 2 to square root of n plus 1),
    # then n is not a prime number
        if (n % i) == 0:
            check_prime = False
            break
    #otherwise, n is a prime number, then print n
    if check_prime:
        print(n, end=" ")
        count = count + 1
        # After printing, keep counting to the next prime number
    n = n + 1 #After printing,keep checking to next integer numbers whether it is prime number or not?
