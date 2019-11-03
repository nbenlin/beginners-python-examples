# Take from the user two-digit number and convert this number to string

first_digit = ["","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
second_digit = ["", "Ten", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

def to_str(num):
    first = num % 10
    second = num // 10

    return second_digit[second] + " " + first_digit[first]

num = int(input("Number:"))
print(to_str(num))
