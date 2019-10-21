"""
First exam has effect %30 to final grade
Second exam has effect %30 to final grade
Final exam has effect %40 to final grade
"""

exam1 = int(input("First exam grade:"))
exam2 = int(input("Second exam grade:"))
final = int(input("Final exam grade:"))

total = exam1 * 3/10 + exam2 * 3/10 + final * 4/10

if total >= 90:
    print("AA")
elif total >= 85:
    print("BA")
elif total >= 80:
    print("BB")
elif total >= 75:
    print("CB")
elif total >= 70:
    print("CC")
elif total >= 65:
    print("DC")
elif total >= 60:
    print("DD")
elif total >= 55:
    print("FD")
else:
    print("FF")
