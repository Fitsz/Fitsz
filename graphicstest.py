import math


prompt = ["What is the first number?: ",
          "What is the second number?: "]

def gcd(first, second):
    if first > second:
        a = first
        b = second
    else:
        a = second
        b = first
    while b > 0:
        c = a % b
        print(a, "floored", b, "is equal to", c)
        a = b
        b = c
    else:
        print("The GCD of your numbers is", a)


while True:
    try:
        a = int(input(prompt[0]))
        b = int(input(prompt[1]))
        break
    except ValueError:
        print("That is not a whole number:")

gcd(a, b)
