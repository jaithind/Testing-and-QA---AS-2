import os

from BMIcalc import BMIcalc
from BMIcategory import BMIcategory

def setHeightFeet():
    positive = False
    while not positive:
        try: 
            height = int(input("Feet: "))
            if height > 0:
                positive = True
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Invalid input. Please enter a positive number.")
            continue
        return height
    
def setHeightInch():
    positive = False
    while not positive:
        try: 
            height = int(input("Inch: "))
            if 0 <= height <= 12:
                positive = True
            else:
                print("Please enter a number between 0 and 12")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 12.")
            continue
        return height

def setWeight():
     positive = False
     while not positive:
        try: 
            weight = int(input("Weight(in pounds): "))
            if weight > 0:
                positive = True
            else:
                print("Please enter a number between 0 and 12")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 12.")
            continue
        return weight

print("Please enter your your height and weight."
      "First the feet, then the inches. Press enter between prompts.")

while True:
    heightFeet = setHeightFeet()
    heightInch = setHeightInch()
    weight = setWeight()
    BMI = BMIcalc(heightFeet, heightInch, weight)
    BMI = str(BMI)
    determine = BMIcategory(BMI)
    
    print("Your BMI is " + BMI + " and your category is "+ determine + ".")
    
   # os.system('cls')
    
    

    

        
    
    
    