def distance_to_origin(x, y):
  
    return (x ** 2 + y ** 2) ** 0.5


x1 = float(input("Введіть координату x для точки A: "))
y1 = float(input("Введіть координату y для точки A: "))
x2 = float(input("Введіть координату x для точки B: "))
y2 = float(input("Введіть координату y для точки B: "))

distance_A = distance_to_origin(x1, y1)
distance_B = distance_to_origin(x2, y2)

if distance_A < distance_B:
    print("Точка A знаходиться ближче до початку координат.")
elif distance_B < distance_A:
    print("Точка B знаходиться ближче до початку координат.")
else:
    print("Точки A і B знаходяться на однаковій відстані до початку координат.")
