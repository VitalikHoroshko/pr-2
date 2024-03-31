a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))
k = int(input("Введіть число k: "))

if a % k == 0:
    print(k, "є дільником числа a.")
if b % k == 0:
    print(k, "є дільником числа b.")
if c % k == 0:
    print(k, "є дільником числа c.")
