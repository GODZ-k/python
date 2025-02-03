fruit = str(input("Please enter your food: "))
color = str(input("Please enter your food color: "))

def checkFruit(fruit,color):
    if fruit == "banana" :
        if color == "green":
            return "unripe"
        elif color == "yellow":
            return "ripe"
        elif color == "brown":
            return "overripe"
        else:
            return "Plase choose right color"
    
print(checkFruit(fruit.casefold() , color.casefold() ))