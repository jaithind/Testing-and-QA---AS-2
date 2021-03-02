import os

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
                    positive = True
                else:
                    print("Please select ")
            except ValueError:
                print("Invalid input. Please select 1 or 2.")
            continue
        
        if choice == 1:
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

            
            heightFeet = setHeightFeet()
            heightInch = setHeightInch()
            weight = setWeight()
            BMI = BMIcalc(heightFeet, heightInch, weight)
            BMI = str(BMI)
            determine = BMIcategory(BMI)
    
            print("Your BMI is " + BMI + " and your category is "+ determine + ".")
            
            
        if choice == 2:
            from savingCalc import savingCalc
            print()
            
    
        if choice == 3:
            loop = False
            break
        
        
        if choice == 0:
            os.system('cls')
            
main()
            
            
            
        
    
    


    
    

    

        
    
    
    