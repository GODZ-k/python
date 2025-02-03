str = "atanmay"
norepeative =""
for i in str:
    repeate = str.count(i)
    if(repeate <= 1):
        norepeative = norepeative + i
        break


print(norepeative)