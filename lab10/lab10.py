# Лабораторная 10.Бирюкова Мария.

from PIL import Image, ImageDraw, ImageFont
import os

def task_10_1():

    input_path = os.path.join('images', 'postcard.jpg')
    print(f'Открываю: {input_path}')
    img = Image.open(input_path)

    width, height = img.size
    print(f'Размер открытки: {width} x {height}')

    # Пример: обрезаем по 40 пикселей со всех сторон
    left = 40
    top = 40
    right = width - 40
    bottom = height - 40

    print(f'Координаты обрезки: left={left}, top={top}, right={right}, bottom={bottom}')

    cropped = img.crop((left, top, right, bottom))
    cropped.save('cropped_postcard.jpg')
    print('Обрезанное изображение сохранено как cropped_postcard.jpg')


def task_10_2():
    holidays = {
        'новый год': 'new_year.jpg',
        'день рождения': 'birthday.jpg',
        '8 марта': 'womens_day.jpg'
    }

    print('Доступные праздники:', ', '.join(holidays.keys()))

    holiday = input('Введите название праздника: ').strip().lower()

    filename = holidays.get(holiday)
    if filename:
        path = os.path.join('images', filename)
        img = Image.open(path)
        img.show()
        print(f'Открытка к празднику "{holiday}" открыта.')
    else:
        print('Такого праздника нет в списке.')



if __name__ == '__main__':
    # task_10_1()
    task_10_2()
    # task_10_3()