height = float(input("Enter your Height in cm:"))
weight = float(input("Enter your weight in kg:"))

BMI = weight / (height/100)**2
print("Your BMI is:" , BMI)

if BMI <= 18.5:
  print("You are underweight")   

elif BMI <= 25:
  print("You are Healthy")

elif BMI <= 30:
  print("You are under weight")

elif BMI <= 35:
    print("You are severly over weight")

elif BMI <= 40:
   print("You are obese")

else :
   print("You are severly obese")


