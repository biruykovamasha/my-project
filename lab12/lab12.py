# Лабораторная 12.Бирюкова Мария.
# Задача 12.1

import json

with open('products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data['products']:
    print(f"Название: {p['name']}")
    print(f"Цена: {p['price']}")
    print(f"Вес: {p['weight']}")

    print("В наличии" if p['available'] else "Нет в наличии!")

    # Заметочки
    # Открыть для чтения ('r'), кодировка utf-8 чтобы русские буквы отображались правильно
    # with закрывает файл после выхода из блока
    # json.load(f) читаем весь файл и превращаем JSON в питоновский словарь
    # в словаре data по ключу 'products' лежит список продуктов, перебираем каждый продукт
    # p - это словарь с ключами
    # f-строка: в {} подставляется значение из p по ключу

# Задача 12.2
import json

with open('products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Текущие продукты:")
for p in data['products']:
    print(f"Название: {p['name']}")
    print(f"Цена: {p['price']}")
    print(f"Вес: {p['weight']}")
    print("В наличии" if p['available'] else "Нет в наличии!")
    print()

name = input("Введите название нового продукта: ")
price = float(input("Цена: "))
weight = float(input("Вес: "))
avail = input("В наличии? (да/нет): ").strip().lower()

available = avail == 'да'

data['products'].append({
    "name": name,
    "price": price,
    "weight": weight,
    "available": available
})

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nОбновлённый список продуктов:")
for p in data['products']:
    print(f"Название: {p['name']}")
    print(f"Цена: {p['price']}")
    print(f"Вес: {p['weight']}")
    print("В наличии" if p['available'] else "Нет в наличии!")
    print()

   # читаем файл, Выводим старые продукты, Спрашиваем новый продукт, Добавляем в список, Сохраняем, Выводим
   # создание словаря нового продукта в append
   # проверка available = avail == 'да' - если ввёл да, будет True, всё остальное - False
#
# # Задача 12.3
#
with open('en-ru.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()         # читаем все строки в список

ru_en = {}

for line in lines:
    line = line.strip()           # удаляем пробелы по краям и символ \n (перенос строки)
    if not line:                  # если строка пустая — пропускаем
        continue

    # Приводим разные типы тире к одному виду для удобства
    line = line.replace(' – ', ' - ').replace('—', '-')
    # проверяем, есть ли в строке разделитель ' - '
    if ' - ' in line:
        # разделяем на две части: английскую и русскую
        eng, rus = line.split(' - ', 1)
        eng = eng.strip()

        # Русская часть может содержать несколько слов через запятую
        rus_words = [w.strip() for w in rus.split(',')]

        # Для каждого русского слова добавляем английский перевод
        for rw in rus_words:
            if rw:  # если слово не пустое
                if rw not in ru_en:
                    ru_en[rw] = set()  # используем множество (set), чтобы избежать дубликатов
                ru_en[rw].add(eng)

    # сортируем русские слова по алфавиту
    sorted_rus = sorted(ru_en.keys())

    # записываем результат в новый файл ru-en.txt
    with open('ru-en.txt', 'w', encoding='utf-8') as f_out:
        for rus_word in sorted_rus:
            # получаем список английских переводов и сортируем их
            eng_list = sorted(ru_en[rus_word])
            # соединяем переводы через запятую с пробелом
            eng_str = ', '.join(eng_list)
            # записываем строку в файл: русское слово - английские слова
            f_out.write(f"{rus_word} – {eng_str}\n")

    print("Файл ru-en.txt успешно создан!")