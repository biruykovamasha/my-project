# Лабораторная 10.Бирюкова Мария.

from PIL import Image, ImageDraw, ImageFont
import os

def task_10_1():

    input_path = os.path.join('images', 'postcard.jpg')
    print(f'Открываю: {input_path}')
    img = Image.open(input_path)

    width, height = img.size
    print(f'Размер открытки: {width} x {height}')

    # обрезаем по 40 пикселей со всех сторон
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


def task_10_3():
    holidays = {
        'новый год': 'new_year.jpg',
        'день рождения': 'birthday.jpg',
        '8 марта': 'womens_day.jpg'
    }

    print('Доступные праздники:', ', '.join(holidays.keys()))
    holiday = input('К какому празднику нужна открытка? ').strip().lower()
    filename = holidays.get(holiday)
    if not filename:
        print('Такого праздника нет.')
        return

    name = input('Введите имя человека, которого поздравляете: ').strip()
    if not name:
        print('Имя не может быть пустым.')
        return

    img_path = os.path.join('images', filename)
    img = Image.open(img_path).convert('RGBA')
    draw = ImageDraw.Draw(img)

    bold_font_path = os.path.join('fonts', 'Roboto-Bold.ttf')
    regular_font_path = os.path.join('fonts', 'Roboto-Regular.ttf')

    if not os.path.exists(bold_font_path) or not os.path.exists(regular_font_path):
        print('Файлы шрифтов не найдены! Проверьте папку fonts/ или путь.')
        return

    font_size = 40
    bold_font = ImageFont.truetype(bold_font_path, font_size)
    regular_font = ImageFont.truetype(regular_font_path, font_size)

    greeting_text = ', поздравляю!'
    name_color = (255, 0, 0)
    greeting_color = (0, 128, 0)

    name_bbox = draw.textbbox((0, 0), name, font=bold_font)
    name_width = name_bbox[2] - name_bbox[0]
    greeting_bbox = draw.textbbox((0, 0), greeting_text, font=regular_font)
    greeting_width = greeting_bbox[2] - greeting_bbox[0]

    total_width = name_width + greeting_width
    img_width, img_height = img.size

    x = (img_width - total_width) // 2
    y = 50

    draw.text((x, y), name, font=bold_font, fill=name_color)
    draw.text((x + name_width, y), greeting_text, font=regular_font, fill=greeting_color)

    output_name = f'greeting_{name}.png'
    img.save(output_name, 'PNG')
    print(f'Поздравительная открытка сохранена как: {output_name}')

if __name__ == '__main__':
    # task_10_1()
    task_10_2()
    # task_10_3()
