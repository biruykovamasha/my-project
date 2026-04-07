# Лабораторная 6.Бирюкова Мария.
# Задание.1
def check(n):
    if n % 3 == 0:
        print(f"{n} делится на 3")
    else:
        print(f"{n} не делится на 3")

n_2 = int(input("Введите число: "))
check(n_2)
#
# # Задание.2
# def d(n):
#     return 100 / n
# try:
#     a = int(input("Введите число, на которое будем делить 100: "))
#     rez = d(a)
#     print(f"Результат: 100 / {a} = {rez}")
# except ValueError:
#     print("Ошибка: нужно вводить только цифры!")
# except ZeroDivisionError:
#     print("Ошибка: на ноль делить нельзя!")
# print("Программа завершена!")
#
# # Задание.3
# def magic_date(date):
#     try:
#         parts = date.split(".")
#         if len(parts) != 3:
#             return False
#         day = int(parts[0])
#         month = int(parts[1])
#         year = int(parts[2])
#
#         year_short = year % 100
#
#         if day * month == year_short:
#             return True
#         else: return False
#
#     except (ValueError, IndexError):
#          return False
#
# print("Программа проверки магической даты.")
# print("Формат: ДД.ММ.ГГГГ (например, 02.11.2022)")
#
# input_date = input("Введите дату: ")
# result = magic_date(input_date)
#
# if result:
#     print(f"Дата {input_date} - магическая!")
# else:
#     print(f"Дата {input_date} - не магическая")
#
# # Задание.4
# def lucky(number):
#     half = len(number) // 2 # половина целочисленная
#     left_sum = 0
#     right_sum = 0
#
#     for d in number[:half]: #d - цифра в строке
#         left_sum = left_sum + int(d)
#
#     for d in number[half:]:
#         right_sum = right_sum + int(d)
#
#     return left_sum == right_sum
#
# ticket = input("Введите номер билета: ")
#
# if len(ticket) % 2 != 0: #четное ли количество цифр
#     print("Номер билета должен содержать чётное количество цифр!")
# else:
#     if lucky(ticket):
#         print("Поздравляю. Билет счастливый!")
#     else:
#         print("Билет не счастливый.")
#
