#calculates the retirement savings
def savingCalc(curAge, salary, perSaved, desGoal):
    curAge = float(curAge)
    salary = float(salary)
    perSaved = float(perSaved)
    desGoal = float(desGoal)
    
    saved = (perSaved/100) * salary
    saved += (35/100) * saved
    goalAge = (desGoal/saved) + curAge
    goalAge = round(goalAge)
    
    return goalAge