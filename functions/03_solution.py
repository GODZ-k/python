def print_all(**kwargs):
    for key , value in kwargs.items():
        print(key, value)

print_all(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10)
print_all(a=1, b=2, c=3)