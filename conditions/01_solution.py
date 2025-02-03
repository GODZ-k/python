age  = int(input("Please enter you age: "))

def checkUserCategory(age):
    if(age < 13):
        return "child"
    elif(13 < age < 19):
        return "Teenager"
    elif(20<age<59):
        return "Adult"
    else:
        return "Senior"
    

print(checkUserCategory(age))

