""" 
Calculate the body mass index according to the height and weight values and print the following texts 
according to these rules. 

Body mass index: kg / length(m) * length(m)

BMI under 18.5 -------> thin
BMI 18.5 to 25 -------> normal
BMI 25 to 30 --------> overweigth
BMI over 30 --------> obese
"""

length = float(input("Length:"))
weigth = int(input("Weigth:"))

bmi = weigth / (length ** 2)

print("Body mass index:", bmi)

if bmi < 18.5:
    print("thin")

elif (bmi >= 18.5 and bmi < 25):
    print("normal")

elif (bmi >= 25 and bmi < 30):
    print("overweight")

else:
    print("obese")










