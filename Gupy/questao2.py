import math

def isPerfectSquare(x):
    square = int(math.sqrt(x))
    return square * square == x

def isFibonacci(n):
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)

number = int(input("Enter a number: "))
if isFibonacci(number):
    print("This number is in the Fibonacci Sequence")
else:
    print("This number is NOT in the Fibonacci Sequence")