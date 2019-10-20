n1 = input("a:")
n2 = input("b:")

print("Values before modification\na: {} b: {}\n".format(n1, n2))

n1,n2 = n2,n1

print("Values after modification\na: {} b: {}\n".format(n1, n2))
