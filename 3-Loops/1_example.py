"""
In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number
itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number.
The sum of divisors of a number, excluding the number itself, is called its aliquot sum, so a perfect number is one that is equal
to its aliquot sum. Equivalently, a perfect number is a number that is half the sum of all of its positive divisors including
itself i.e.
σ1(n) = 2n. For instance, 28 is perfect as 1 + 2 + 4 + 7 + 14 + 28 = 56 = 2 × 28. 
"""

num = int(input("Number:"))

i = 1
sum = 0
while(i < num):
    if(sayi % i == 0):
        sum += 1
    i += 1

if sum == num:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
