height = input("Enter your heigth in m:\n")
weight = input("Enter your weight in kg:\n")

h = float(height)
w = int(weight)

bmi = w / h ** 2
result = int(bmi)
print("As int" , result)

result = round(bmi) 

print("Before the round fuction", bmi)
print("As round fuction ", result)