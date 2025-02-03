year = int(input("enter your year: "))

def checkLeapyear(year):
    if (year % 400 == 0) or  (year % 4 ==0 and year % 100 != 0):
        return "Leap year"
    else:
        return "Not leap year"
    
print(checkLeapyear(year))
