#calculates the BMI
def BMIcalc(heightFeet, heightInch, weight):
    heightFeet = float(heightFeet)
    heightInch = float(heightInch)
    weight = float(weight)
    kilos = weight * 0.45
    hInch = heightInch + (heightFeet * 12)
    hInch = hInch * 0.025
    BMI = (kilos/ (hInch * hInch))
    BMI = round(BMI, 1)
    return BMI