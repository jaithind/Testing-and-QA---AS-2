#validates the user to input positive numbers
def getPosValue(name):
            positive = False
            while not positive:
                try: 
                    value = int(input(name + ": "))
                    if value > 0:
                        positive = True
                    else:
                        print("Please enter a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a positive number.")
                    continue
            return value