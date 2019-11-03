#Find the numbers divided by 3 from 1 to 100.

for i in range(1, 101):
    if i % 3 != 0:
        continue
    print(i)
       
