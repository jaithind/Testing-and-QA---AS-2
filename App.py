# To execute this file type the following in a ternmainal: 
# python App.py
import os
from getPosValue import getPosValue
from BMIcalc import BMIcalc
from BMIcategory import BMIcategory
from savingCalc import savingCalc

def main():
    
    #loop for the menu
    loop = True
    while loop:
        print("Enter 1 for BMI")
        print("Enter 2 for Retirement function")
        print("Enter 3 to exit")
        print("Enter 0 to clear the screen")
        
        #check for valid menu choices
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
        
        #validation for user inches input
        def getHeightInch():
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
        
        #implementation of the BMI calculator
        if choice == 1:
            
            
            print("Please enter your your height and weight."
                " First the feet, then the inches. Press enter between prompts.")
            
            heightFeet = getPosValue("Feet")
            heightInch = getHeightInch()
            weight = getPosValue("Weight")
            BMI = BMIcalc(heightFeet, heightInch, weight)
            determine = BMIcategory(BMI)
            BMI = str(BMI)
    
            print("Your BMI is " + BMI + " and your category is "+ determine + ".")
            print(" ")
            
            
        #implementation of the retirement savings calculator
        if choice == 2:
           
            print("Please enter the follwing fields.")
            
            curAge = getPosValue("Current Age")
            salary = getPosValue("Salary")
            perSaved = getPosValue("Percentage Saved. Please enter as a percent value without symbol")
            desGoal = getPosValue("Desired Goal")
            goal = savingCalc(curAge, salary, perSaved, desGoal)
            
            if goal < 100:
                goal = str(goal)
                print("Your age when you meet your goal will be " + goal)
                print(" ")
            else:
                print("You will not meet your goal before death. The age at which you would meet your goal is " + str(goal) + ".")
                print(" ")
                
        #exit the app
        if choice == 3:
            loop = False
            break
        # clear the screen
        if choice == 0:
            os.system('cls')
            
main()