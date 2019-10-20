# Get three numbers from the user and print the largest number.

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a >= b and a >= c:
    print("Largest element is a : {}".format(a))
elif b >= a and b >= c:
    print("Largest element is b : {}".format(b))
elif c >= a and c >= b:
    print("Largest element is c : {}".format(c)) 
