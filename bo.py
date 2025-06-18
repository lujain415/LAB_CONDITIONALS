a=float(input("What is your weight? "))
b=float(input("How tall are you? "))
bmi=a/b**2
print(round(bmi,2))
if bmi>=25:
    print("You are overwieght you need to work out more and watch your diet.")
elif bmi>=18:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")