# Лабораторная 11.Бирюкова Мария.
# Задача 11.1
import os
from PIL import Image, ImageFilter


def task_11_1():
    in_dir = 'images'  # откуда берём
    out_dir = 'filtered'  # куда сохраняем

    # 1. Создаём папку для результата
    os.makedirs(out_dir, exist_ok=True)

    # 2. Обходим все файлы в папке
    for name in os.listdir(in_dir):
        path_in = os.path.join(in_dir, name)

        # Пропускаем папки, ищем файлы
        if not os.path.isfile(path_in):
            continue

        # Обрабатываем картинки
        if name.lower().endswith(('.jpg', '.jpeg', '.png')):
            img = Image.open(path_in)

            # размытие
            processed = img.filter(ImageFilter.GaussianBlur(radius=3))

            # Сохраняем в новую папку
            processed.save(os.path.join(out_dir, name))
            print(f'Готово: {name}')

# Задача 11.2
def task_11_2():
    folder = 'images'
    allowed = ('.jpg', '.jpeg', '.png')  # Разрешённые расширения

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        # файл И нужное расширение
        if os.path.isfile(path) and filename.lower().endswith(allowed):
            img = Image.open(path)
            print(f'Открыт: {filename} | {img.width}x{img.height}px')
        else:
            print(f'Пропущен: {filename}')

# Задача 11.3
import csv


def task_11_3():
    total = 0
    print('Нужно купить:')

    # Открываем CSV-файл
    with open('shop.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Пропускаем первую строку с заголовками

        for row in reader:
            product = row[0]  # Название товара
            count = int(row[1])  # Количество (превращаем текст в число)
            price = int(row[2])  # Цена (превращаем текст в число)

            total += count * price
            print(f'{product} - {count} шт. за {price} руб.')

    print(f'\nИтоговая сумма: {total} руб.')

if __name__ == '__main__':

    task_11_1()
    # task_11_2()
    # task_11_3()