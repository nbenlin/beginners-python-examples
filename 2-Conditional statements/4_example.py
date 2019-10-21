# First ask to user to choice triangle or quadrilateral.
# If user will choice rectengular ask to user for edges of rectangle
# Then find is it square, rectangle or quadrilateral

# If users choice will be triangle then ask to user for edges of triangle
# And find is it isosceles, equilateral triangle or just triangle
# If it can't be triangle write on the screen triangle does not specify

# U can use abs() function to find the absolute value.
# -------------------------------------------------------------------------------

form = input("Your choice is triangle or quadrilateral?")

if form == "quadrilateral":
    print("Please enter the edges.")
    edge1 = int(input("Edge 1:"))
    edge2 = int(input("Edge 2:"))
    edge3 = int(input("Edge 3:"))
    edge4 = int(input("Edge 4:"))

    if edge1 == edge2 and edge1 == edge3 and edge1 == edge4:
        print("It's square")
    elif (edge1 == edge3 and edge2 == edge4):
        print("It's rectangle")
    else:
        print("It's just quadrilateral")

elif form == triangle:
    edge1 = int(input("Edge 1:"))
    edge2 = int(input("Edge 2:"))
    edge3 = int(input("Edge 3:"))
    if abs(edge1 + edge2) > edge3 and abs(edge1 + edge3) > edge2 and abs(edge2 + edge3) > edge1:
        if edge1 == edge2 and edge1 == edge3:
            print("It's equilateral triangle...")
        elif (edge1 == edge2 and edge1 != edge3) or (edge1 == edge3  and edge1 != edge2) or (edge2 == edge3 and edge2 != edge1):
            print("It's isosceles...")
        else:
            print("It's scalene triangle...")
    else:
        print("It's not a triangle...")

else:
    print("Invalid form...")
