def BMIcategory(BMI):
    BMI = float(BMI)
    if BMI<18.5:
        result = "Underweight"
        return result
    elif 18.5<=BMI<=24.9:
        result = "Normal weight"
        return result
    elif 25<=BMI<=29.9:
        result = "Overweight"
        return result
    elif BMI>=30:
        result = "Obese"
        return result