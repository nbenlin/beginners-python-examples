# Take a number from the user and try to find is it Armstrong number.
# Example to Armstrong number 1634 = 1^4 + 6^4 + 3^4 + 4^4

num = input("Number:")
num_of_digits = len(num)
num = int(num)
digit = 0
sum = 0

tmp_num = num

while tmp_num > 0:
    digit = tmp_num % 10
    sum += digit ** num_of_digits
    tmp_num //= 10

if sum == num:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")
