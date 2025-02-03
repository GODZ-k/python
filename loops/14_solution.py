items = ["apple","orange","banana","apple","mango","mango"]

uniqueItem = set()
count = 0


for item in items:
    if item in uniqueItem:
       print(item)
    uniqueItem.add(item)
