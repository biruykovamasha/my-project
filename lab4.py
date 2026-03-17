#Лабораторная 4.Бирюкова Мария.
#Задание.1
password1 = input("Введите пароль: ")
password2 = input("Повторите пароль: ")
if password1 == "" or password2 == "":
    print("Ошибка: пароль не может быть пустым")
elif password1 == password2:
    print("Пароль принят")
else:
    print("Пароль не принят")

#Задание.2
place = int(input("Введите номер места (1-54): "))
if place < 1 or place > 54:
        print("Ошибка: такого места в вагоне нет")
else:
    if place >= 37:
        place_type = "боковое"
    else:
        place_type = "купейное"
    if place % 2 == 0:
        level = "верхнее"
    else:
        level = "нижнее"
    print("Место", place,":", level,",", place_type)

#Задание.3
year = int(input("Введите год: "))
if year <= 0:
    print("Ошибка: год должен быть положительным числом!")
else:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Год", year, "- високосный")
    else:
        print("Год", year, "- не високосный")

#Задание.4
color1 = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")
valid_colors = ["красный", "Красный", "синий", "Синий", "желтый", "Желтый"]
if color1 not in valid_colors or color2 not in valid_colors:
    print("Неверный цвет")
else:
    if color1 == color2:
        print("Результат:", color1)
    elif(color1 == "красный" or color1 == "Красный") and (color2 == "синий" or color2 == "Синий"):
        print("Результат: фиолетовый")
    elif (color1 == "красный" or color1 == "Красный") and (color2 == "желтый" or color2 == "Желтый"):
        print("Результат: оранжевый")
    elif (color1 == "синий" or color1 == "Синий") and (color2 == "желтый" or color2 == "Желтый"):
        print("Результат: зелёный")