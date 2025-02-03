number = int(input("PLEASE ENTER YOUR NUMBER: "))

isPerime = False

if number > 1:
   for i in range(2, number):
    if (number % i) == 0:
        isPerime = False
        break
    else:
        isPerime = True

print(isPerime)
