x = float(input("Введіть число x: "))
y = float(input("Введіть число y: "))

if x != y:
    min_number = min(x, y)
    max_number = max(x, y)

    x = (min_number + max_number) / 2
    y = min_number * max_number * 2

    print("Після заміни:")
    print("x =", x)
    print("y =", y)
else:
    print("Числа x та y повинні бути різними.")
