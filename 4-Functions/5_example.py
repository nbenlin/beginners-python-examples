# Find the numbers from 1 to 100 which can create Pythagorean triple.

def pythagorean_triple():
    
    pythagorean_list = list()
    for i in range(1, 101):
        for j in range(1, 101):
            
            c = (i ** 2 + j ** 2) ** 0.5
            if c == int(c):
                pythagorean_list.append((i, j, int(c)))
    return pythagorean_list

for i in pythagorean_triple():
    print(i)

