number = int(input("Plese enter your number: "))
sum = 0
count = 0

for n in range(1,number+1):
    if(n%2==0):
        sum = sum + n
        count +=1
    
print(sum , count)