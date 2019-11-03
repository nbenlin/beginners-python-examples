# Find the perfect numbers from 1 to 1000. Create a function for check numbers.

def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

for i in range(1, 1001):
    if(perfect_number(i)):
        print("Perfect Number:", i)
