#Лабораторная 6.Бирюкова Мария.
#Задание.1
def check_number(n):
    if number % 3 == 0:
        print(f"{n} делится на 3")
    else:
        print(f"{n} не делится на 3")

num = int(input("Введите число: "))
check_number(num)

#Задание.2
def divide_100(num):
    try:
        res = 100 / num
        print(f"Результат: 100 / {num} = {res}")
    except ZeroDivisionError:
        print("Ошибка: на ноль делить нельзя!")
try:
    user_input = input("Введите число, на которое будем делить: ")
    num = int(user_input)
    divide_100(num)
except ValueError:
    print("Ошибка: нужно вводить только цифры!")

#Задание.3
def magic_date(date):
    try:
        parts = date.split(".")
        if len(parts) != 3:
            return False
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])

        year_short = year % 100

        if day * month == year_short:
            return True
        else:
            return False

     except (ValueError, IndexError):
         return False

print("Программа проверки магической даты.")
print("Формат: ДД.ММ.ГГГГ (например, 02.11.2022)")

input_date = input("Введите дату: ")
result = magic_date(input_date)

if result:
    print(f"Дата {input_date} - магическая!")
else:
    print(f"Дата {input_date} - не магическая")
