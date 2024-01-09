# 🚨 This program interprets the Body Mass Index (BMI) based on a user's weight and height.

# inputs
height = float(input("Enter your height in meters e.g., 1.55: "))
weight = int(input("Enter your weight in kilograms e.g., 72: "))


# operation 👇
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
bmi = (weight / (height ** 2))

# if statements
if (bmi < 18.5):
  print(f"Your BMI is {bmi}, you are underweight.")
elif (bmi > 18.5 and bmi<25):
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif (bmi >= 25 and bmi < 30):
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif (bmi >= 30 and bmi < 35):
  print(f"Your BMI is {bmi}, you are obese.")
elif (bmi >= 35):
  print(f"Your BMI is {bmi}, you are clinically obese.")