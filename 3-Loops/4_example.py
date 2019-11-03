# Take a number from user with using the loop and add these numbers until user will enter 'q'

sum = 0

while True:
    num = input("Number:")

    if num == "q":
        break
    num = int(num)
    sum += num
print("Sum of number:", sum)
