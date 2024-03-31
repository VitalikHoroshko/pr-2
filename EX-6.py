a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

if a != b:

    if a > b:
        b = a
    else:
        a = b
else:

    a = b
    b = a

print("Після заміни:")
print("a =", a)
print("b =", b)
