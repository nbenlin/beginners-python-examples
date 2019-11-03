# Take two numbers from the user and find greatest common divisor of these numbers.

def find_gcd(num1, num2):
    i = 1
    gcd = 1
    while i <= num1 and i <= num2:
        if not (num1 % i) and not (num2 % i):
            gcd = i
        i += 1
    return gcd

num1 = int(input("Number-1:"))
num2 = int(input("Number-2:"))

print("Greatest common divisor:", find_gcd(num1, num2))
