number = [1,-2,3,4,5,-6,-7,-8,9,-10]
count = 0
for item in number:
    if(item >= 0):
       count +=1
       print(item)

print("count",count)