import time
waittime = 1
retries = 5
attempt = 0

while attempt < retries:
    print("attempt" , attempt +1 ,"-wait",waittime)
    time.sleep(waittime)
    waittime *=2
    attempt +=1
