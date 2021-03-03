import os
from getPosValue import getPosValue
from BMIcalc import BMIcalc
from BMIcategory import BMIcategory
from savingCalc import savingCalc

def main():
    
    loop = True
    while loop:
        print("Enter 1 for BMI")
        print("Enter 2 for Retirement function")
        print("Enter 3 to exit")
        print("Enter 0 to clear the screen")
        
        positive = False
        while not positive:
            try: 
                choice = int(input("Enter your choice: "))
                if 0 <= choice <= 3:
                    print(" ")
                    positive = True
                else:
                    print("Please select between the available choices.")
            except ValueError:
                print("Invalid input. Please select between the available choices.")
            continue
        
        
        
        if choice == 1:
            
            
            print("Please enter your your height and weight."
                " First the feet, then the inches. Press enter between prompts.")
            
            heightFeet = getPosValue("Feet")
            heightInch = getPosValue("Inches")
            weight = getPosValue("Weight")
            BMI = BMIcalc(heightFeet, heightInch, weight)
            determine = BMIcategory(BMI)
            BMI = str(BMI)
    
            print("Your BMI is " + BMI + " and your category is "+ determine + ".")
            print(" ")
            
            
            
        if choice == 2:
           
            print("Please enter the follwing fields.")
            
            curAge = getPosValue("Current Age")
            salary = getPosValue("Salary")
            perSaved = getPosValue("Percentage Saved")
            desGoal = getPosValue("Desired Goal")
            goal = savingCalc(curAge, salary, perSaved, desGoal)
            
            if goal < 100:
                goal = str(goal)
                print("Your age when you meet your goal will be " + goal)
                print(" ")
            else:
                print("You will not meet your goal before death.")
                print(" ")
            
        if choice == 3:
            loop = False
            break
        
        if choice == 0:
            os.system('cls')
            
main()