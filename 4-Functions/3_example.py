# Take two numbers from the user and find least common multiple of these numbers.

def find_lcm(num1, num2):
    i = 2
    lcm = 1
    while True:
        if num1 % i == 0 and num2 % i == 0:
            lcm *= i

            num1 //= i
            num2 //= i
        
        elif num1 % i == 0 and num2 % i != 0:
            lcm *= i
            
            num1 //= i
        
        elif num1 % i != 0 and num2 % i == 0:
            lcm *= i

            num2 //= i
        
        else:
            i += 1
        
        if num1 == 1 and num2 == 1:
            break
    return lcm

num1 = int(input("Number-1:"))
num2 = int(input("Number-2:"))

print("Least common multiple:", find_lcm(num1, num2))
