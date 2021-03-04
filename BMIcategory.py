#returns the ctaegory of the BMI calculated
def BMIcategory(BMI):
    result = ""
    if BMI<18.5:
        result = "Underweight"
        
    elif 18.5<=BMI<=24.9:
        result = "Normal Weight"
    
    elif 25<=BMI<=29.9:
        result = "Overweight"
        
    elif BMI>=30:
        result = "Obese"
    return result