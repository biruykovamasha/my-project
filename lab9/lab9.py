# Лабораторная 9.Бирюкова Мария.
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw, ImageFont
import os

IMG_DIR = 'images'

def task_9_1():
    filename = os.path.join('images', 'cat.jpg')
    img = Image.open(filename)
    img.show()

    width, height = img.size
    fmt = img.format
    mode = img.mode

    print('Задача 9.1')
    print(f'Размер: {width} x {height}')
    print(f'Формат: {fmt}')
    print(f'Цветовая модель: {mode}')


def task_9_2():
    filename = os.path.join('images', 'image.jpg')

    img = Image.open(filename)

    # 1. Уменьшенная в три раза копия
    w, h = img.size
    new_w = w // 3
    new_h = h // 3
    small_img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    small_img.save('small_image.jpg')

    # 2. Горизонтальный зеркальный образ (слева направо)
    h_flip = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    h_flip.save('horizontal_flip.jpg')

    # 3. Вертикальный зеркальный образ (сверху вниз)
    v_flip = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    v_flip.save('vertical_flip.jpg')

    print('Задача 9.2 выполнена. Сохранены файлы:')
    print('  small_image.jpg')
    print('  horizontal_flip.jpg')
    print('  vertical_flip.jpg')


def task_9_3():

    # Убеждаемся, что папка filtered существует
    os.makedirs('filtered', exist_ok=True)

    # Выбираем фильтр EMBOSS – тиснение
    filter_type = ImageFilter.EMBOSS

    # Обрабатываем 5 файлов
    for i in range(1, 6):
        input_path = os.path.join('images', f'{i}.jpg')

        img = Image.open(input_path)

        filtered_img = img.filter(filter_type)

        output_path = os.path.join('filtered', f'filtered_{i}.jpg')

        filtered_img.save(output_path)
        print(f'Обработан: {input_path} -> {output_path}')

    print('Задача 9.3 выполнена. Файлы сохранены в папке filtered.')


def task_9_4():

    os.makedirs('watermarked', exist_ok=True)

    watermark_text = "Watermark"

    files_to_process = ['photo1.jpg', 'photo2.jpg']

    for fname in files_to_process:
        input_path = os.path.join('images', fname)
        # Открываем и переводим в RGBA, чтобы можно было смешивать с прозрачным слоем
        img = Image.open(input_path).convert('RGBA')

        # Создаём прозрачный слой такого же размера
        txt_layer = Image.new('RGBA', img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)

        # Шрифт
        font = ImageFont.load_default()
        # Цвет текста
        text_color = (255, 255, 255, 128)

        # Определяем размеры текста
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Позиция: правый нижний угол с отступом 10 пикселей
        margin = 10
        x = img.size[0] - text_width - margin
        y = img.size[1] - text_height - margin

        # Рисуем текст на прозрачном слое
        draw.text((x, y), watermark_text, font=font, fill=text_color)

        # Совмещаем оригинал и слой с текстом
        watermarked = Image.alpha_composite(img, txt_layer)

        # Сохраняем результат в папку watermarked (в PNG, чтобы сохранить прозрачность)
        output_path = os.path.join('watermarked', f'wm_{fname}')
        watermarked.save(output_path, 'PNG')
        print(f'Водяной знак добавлен: {input_path} -> {output_path}')

    print('Задача 9.4 выполнена. Файлы сохранены в папке watermarked.')

if __name__ == '__main__':
    task_9_1()
    # task_9_2()
    # task_9_3()
    # task_9_4()



