# Лабораторная 6.Бирюкова Мария.
# # Задание.1
# numbers = [3, 5, 7, 2, 9]
# user_numbers = int(input("Введите число: "))
# print("Исходный список: ", numbers)
# print("Введённое число: ", user_numbers)
# if user_numbers in numbers:
#     print("Поздравляю, Вы угадали число!")
# else:
#     print("Нет такого числа!")

# # Задание.2
# numbers = [3, 5, 3, 7, 2, 9, 7]
# unic = set() #set() - пустое множество УНИКАЛЬНЫХ знач
# duplicates = set()
# for element in numbers:
#     if element in unic:
#         duplicates.add(element)
#     else:
#         unic.add(element)
# if duplicates:
#     print("Найдены повторяющиеся элементы: ", list(duplicates))
# else:
#     print("Повторяющихся элементов нет.")

# # Задание.3
# week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
# weekends_count = int(input("Сколько выходных дней на неделе вы хотите? "))
#
# if weekends_count > 0:
#     weekends = week[-weekends_count:]
# else:
#     weekends = []
#
# if weekends_count == 0:
#     workdays = week[:]        # Все дни
# elif weekends_count == 7:
#     workdays = []
# else:
#     workdays = week[:-weekends_count]
#
# print("Ваши выходные дни:", ", ".join(weekends) if weekends else "нет")
# print("Ваши рабочие дни:", ", ".join(workdays) if workdays else "нет")

# Задание.4
group_1 = ["Аминов", "Бирюкова", "Грищенко", "Гудеев", "Дворянинова",
      "Заец", "Клименко", "Красноперов", "Меркурьев", "Пархоменко"]
group_2 = ["Светлакова", "Седова", "Царьков", "Цыбульская", "Чувашова",
      "Чурсина", "Шайдурова", "Шаламова", "Ярмола", "Егоров"]

import random

g_1 = random.sample(group_1, 5)

g_2 = random.sample(group_2, 5)

team = tuple(g_1 + g_2)

print("Исходный список Вашей группы:", group_1)
print("Исходный список другой группы:", group_2)
print("Спортивная команда (кортеж):", team)

print("Длина кортежа (количество человек в команде):", len(team))

team_sorted = tuple(sorted(team))
print("Отсортированный кортеж по алфавиту:", team_sorted)

surname = "Бирюкова"
count = team.count(surname)

if count > 0:
    print(f'Студент "{surname}" входит в команду.')
    print(f'Фамилия "{surname}" встречается {count} раз(а).')
else:
    print(f'Студент "{surname}" не входит в команду.')