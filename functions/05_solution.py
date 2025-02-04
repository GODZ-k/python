def even_generator(n):
    for i in range(n):
       yield i

print(even_generator(10))
item = even_generator(10)
for i in item:
    print(i)