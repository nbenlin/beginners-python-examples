# Take the two perpendicular sides (a, b) of a right triangle from the user and try to find the length of the hypotenuse.

a = int(input("a: "))
b = int(input("b: "))
c = (a ** 2 + b ** 2) ** 0.5

print("Hypotenuse: ", c)
