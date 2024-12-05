rectangle_length = float(input("Введите длину прямоугольника: "))
rectangle_width = float(input("Введите ширину прямоугольника: "))

rectangle_perimeter = 2 * (rectangle_length + rectangle_width) 
rectangle_area = round(rectangle_length * rectangle_width, 2)

print(f"\nПериметр прямоугольника равен = {rectangle_perimeter}")
print(f"Площадь прямоугольника равна = {rectangle_area}", end = '\n\n')