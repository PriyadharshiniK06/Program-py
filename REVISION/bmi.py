weight=int(input("Enter your weight: "))
height=float(input("Enter your height: "))
bmi=weight/(height*height)
if(bmi<18.5):
    print("Underweight")
elif(bmi>=18.5 and bmi<=24.9):
    print("Normal")
elif(bmi>=25 and bmi<=29.9):
    print("Overweight")
else:
    print("Obese")