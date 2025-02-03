size = str(input("please enter you coffie size: "))
extrashoot = str(input("do you want extra shoot say yes or no: "))

def customizeCoffee(size,extrashoot):
    if extrashoot == "yes":
        output = "Coffee with {} have extrashoot"
        return output.format(size)
    else:
        output = "Coffee with {} have no extrashoot"
        return output.format(size)
    
print(customizeCoffee(size.casefold() , extrashoot.casefold()))