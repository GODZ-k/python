day = "wednesday"
age  = int(input("Please enter your age: "))
def checkPrice(age ,day):
    price = 12 if age > 18 else  8
    if day == "wednesday":
        price = price - 2
        return price 

print(checkPrice(age , day))